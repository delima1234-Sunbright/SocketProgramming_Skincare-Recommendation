import socket
import pandas as pd
import json

def read_data_from_excel(file_path):
    df = pd.read_excel(file_path, sheet_name='Products')
    print("Data from Excel loaded successfully")
    return df

def get_recommendations(skin_type, budget, df):
    categories = ["Facewash", "Toner", "Serum", "Moisturizer", "Sunscreen"]
    recommendations = {category: [] for category in categories}
    total_price = 0
    for index, data in df.iterrows():
        if (data["Jenis Kulit"].lower() == skin_type.lower() and 
            data["Harga"] <= budget - total_price):
            
            product = {
                "Category": data["Category"],
                "products": data["products"],
                "Bahan Aktif": data["Bahan Aktif"],
                "Kegunaan": data["Kegunaan"],
                "Harga": data["Harga"],
                "Rating": data["Rating"]
            }
            if is_compatible(data["Bahan Aktif"].split(', '), recommendations):
                if data["Category"] in recommendations:
                    recommendations[data["Category"]].append(product)
                    total_price += data["Harga"]
                    if total_price >= budget:
                        break  
    return recommendations, total_price

# Fungsi untuk memeriksa kompatibilitas bahan aktif
def is_compatible(ingredients, recommendations):
    incompatible_pairs = [
        ("Glycerin", "Hyaluronic Acid"),
        ("Salicylic Acid", "AHA,BHA,PHA"),
        ("Niacinamide", "Vitamin C"),
        ("Pro-Retinol", "Salicylic Acid"),
        ("Witch Hazel", "AHA,BHA,PHA"),
        ("Zinc Oxide", "Niacinamide"),
        ("Vitamin C", "Vitamin E, Jojoba Oil"),
        ("Green Tea Extract", "Centella Asiatica")
    ]
    
    for category, products in recommendations.items():
        for product in products:
            product_ingredients = product['Bahan Aktif'].split(', ')
            for pair in incompatible_pairs:
                if (pair[0] in ingredients and pair[1] in product_ingredients) or (pair[1] in ingredients and pair[0] in product_ingredients):
                    return False
    return True

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.10.176.22', 8080))
server_socket.listen(5)

print('Waiting for connection')

excel_file = 'Data Skincare.xlsx'
df = read_data_from_excel(excel_file)

while True:
    client_socket, client_address = server_socket.accept()
    print('Connection accepted from:', client_address)
    data = client_socket.recv(4096).decode()
    if not data:
        break

    user_data = json.loads(data)
    skin_type = user_data['skin_type']
    budget = user_data['budget']
    print(f'Requested skin type: {skin_type}, budget: {budget}')
    recommendations, total_price = get_recommendations(skin_type, budget, df)
    response_data = {"recommendations": recommendations, "total_price": total_price}
    client_socket.sendall(json.dumps(response_data).encode())
    client_socket.close()
