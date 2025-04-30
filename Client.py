import socket
import json

# Fungsi untuk mengirim data dan menerima respons dari server
def send_data_and_receive_response(data, server_address=('localhost', 8080)):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    client_socket.sendall(json.dumps(data).encode())

    buffer = ""
    while True:
        response = client_socket.recv(4096).decode()
        if not response:
            break
        buffer += response

    client_socket.close()

    # Mengurai respons JSON
    try:
        response_data = json.loads(buffer)
        recommendations = response_data.get("recommendations", {})
        total_price = response_data.get("total_price", 0)

        print(f"Total price of recommended products: {total_price}\n")

        for category, products in recommendations.items():
            if products:
                print(f"{category}:")
                for i, product in enumerate(products, start=1):
                    print(f"Product {i}: {product['products']} ({product['Category']})")
                    print(f" - Kegunaan: {product['Kegunaan']}")
                    print(f" - Bahan Aktif: {product['Bahan Aktif']}")
                    print(f" - Harga: {product['Harga']}")
                    print(f" - Rating: {product['Rating']}\n")
    except json.JSONDecodeError:
        print("Failed to decode response from server.")

# Meminta input dari pengguna
skin_type = input("Masukkan jenis kulit Anda (normal, kering, berminyak, sensitif, kombinasi): ")
budget = float(input("Masukkan budget Anda: "))

# Data yang akan dikirim ke server
data = {
    "skin_type": skin_type,
    "budget": budget
}

# Mengirim data ke server dan menerima respons
send_data_and_receive_response(data)

# Menanyakan kepada pengguna apakah ingin mengetahui cara penggunaan produk
cara_penggunaan = input("Apakah kamu ingin mengetahui bagaimana cara menggunakannya? (ya/tidak): ").strip().lower()

if cara_penggunaan == 'ya':
    cara_penggunaan_produk = """
    Facewash:
    1. Basahi wajah.
    2. Aplikasikan facewash dan gosok lembut.
    3. Bilas dengan air hangat dan keringkan dengan handuk lembut.

    Toner:
    1. Tuangkan toner ke kapas atau telapak tangan.
    2. Usapkan ke seluruh wajah dan leher.
    3. Biarkan meresap sebelum lanjut ke langkah berikutnya.

    Serum:
    1. Ambil sedikit serum dan usapkan ke wajah dan leher.
    2. Biarkan meresap sebelum langkah selanjutnya.

    Pelembab:
    1. Ambil pelembab dan aplikasikan merata ke wajah dan leher.
    2. Tepuk-tepuk lembut untuk penyerapan.

    Sunscreen:
    1. Gunakan sunscreen dengan SPF sesuai kebutuhan.
    2. Aplikasikan sebelum keluar dan ulangi setiap 2 jam.
    """
    print(cara_penggunaan_produk)
