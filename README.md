# Skincare Recommendation System using Socket Programming

**Overview**

This project is a **Socket Programming** application developed in *Python* that enables communication between a client and a server to provide personalized **skincare product recommendations**. The system recommends products based on the user's *skin type*, *budget*, and *skincare categories* (Facewash, Toner, Serum, Moisturizer, Sunscreen). It ensures compatibility of active ingredients to avoid harmful combinations and stays within the user's budget.

**Link to Repository**: [Skincare Recommendation System](https://github.com/delima1234-Sunbright/SocketProgramming_Skincare-Recommendation)

## Features

- **Client-Server Communication**: Uses *TCP sockets* for reliable data exchange between client and server.
- **Personalized Recommendations**: Recommends products based on:
  - *Skin type* (normal, dry, oily, sensitive, combination).
  - *Budget* (user-specified amount).
  - *Product categories* (Facewash, Toner, Serum, Moisturizer, Sunscreen).
- **Ingredient Compatibility**: Checks for incompatible active ingredient pairs (e.g., Niacinamide and Vitamin C) to ensure safe recommendations.
- **Excel Data Integration**: Reads product data from an Excel file (`Data Skincare.xlsx`) using *pandas*.
- **Usage Instructions**: Optionally provides step-by-step guidance on how to use recommended products.
- **JSON Data Exchange**: Uses *JSON* for structured data transfer between client and server.

## Project Structure

- **Client Code** (`client.py`):
  - Collects user input (skin type and budget).
  - Sends data to the server via a TCP socket.
  - Receives and displays recommendations, including product details (name, category, active ingredients, usage, price, rating).
  - Optionally displays product usage instructions if requested by the user.

- **Server Code** (`server.py`):
  - Listens for client connections on a specified IP and port (`10.10.176.22:8080`).
  - Reads product data from an Excel file.
  - Processes client requests to generate recommendations based on skin type and budget.
  - Ensures ingredient compatibility and budget constraints.
  - Sends recommendations back to the client in JSON format.

- **Excel File** (`Data Skincare.xlsx`):
  - Contains product data with columns: `Jenis Kulit` (skin type), `Category`, `products`, `Bahan Aktif` (active ingredients), `Kegunaan` (usage), `Harga` (price), `Rating`.

## How It Works

1. **Client Side**:
   - The user inputs their *skin type* and *budget*.
   - The client sends this data as a JSON object to the server.
   - The client receives recommendations, displays product details, and shows the total price.
   - If the user chooses, it displays instructions for using each product category.

2. **Server Side**:
   - Loads product data from `Data Skincare.xlsx` using *pandas*.
   - Listens for client connections and receives JSON data (skin type, budget).
   - Filters products by skin type and budget, ensuring the total price stays within the budget.
   - Checks active ingredient compatibility to avoid harmful combinations.
   - Returns a JSON response with recommendations and total price.

3. **Ingredient Compatibility**:
   - The server checks for incompatible ingredient pairs (e.g., Salicylic Acid with AHA/BHA/PHA) to ensure safe product combinations.

## Requirements

- **Python 3.x**
- **Libraries**:
  - `socket` (built-in)
  - `json` (built-in)
  - `pandas` (for Excel file handling)
  - `openpyxl` or `xlrd` (for reading Excel files)
- **Excel File**: `Data Skincare.xlsx` with the required product data.

Install dependencies using:
```bash
pip install pandas openpyxl
```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/delima1234-Sunbright/SocketProgramming_Skincare-Recommendation.git
   cd SocketProgramming_Skincare-Recommendation
   ```

2. **Prepare the Excel File**:
   - Ensure `Data Skincare.xlsx` is in the project directory.
   - The Excel file should have a sheet named `Products` with columns: `Jenis Kulit`, `Category`, `products`, `Bahan Aktif`, `Kegunaan`, `Harga`, `Rating`.

3. **Run the Server**:
   - Update the server IP in `server.py` if needed (default: `10.10.176.22`).
   - Start the server:
     ```bash
     python server.py
     ```

4. **Run the Client**:
   - Ensure the server is running.
   - Update the server address in `client.py` if needed (default: `localhost`, port `8080`).
   - Run the client:
     ```bash
     python client.py
     ```

5. **Interact with the Client**:
   - Enter your skin type (e.g., `normal`, `kering`, `berminyak`, `sensitif`, `kombinasi`).
   - Enter your budget (e.g., `500000`).
   - View the recommended products and total price.
   - Choose whether to see product usage instructions (`ya` or `tidak`).

## Example Usage

**Server Output**:
```
Waiting for connection
Data from Excel loaded successfully
Connection accepted from: ('127.0.0.1', 54321)
Requested skin type: berminyak, budget: 500000
```

**Client Input**:
```
Masukkan jenis kulit Anda (normal, kering, berminyak, sensitif, kombinasi): berminyak
Masukkan budget Anda: 500000
```

**Client Output**:
```
Total price of recommended products: 450000

Facewash:
Product 1: Cleanser X (Facewash)
 - Kegunaan: Membersihkan minyak berlebih
 - Bahan Aktif: Salicylic Acid
 - Harga: 100000
 - Rating: 4.5

Toner:
Product 1: Toner Y (Toner)
 - Kegunaan: Mengontrol sebum
 - Bahan Aktif: Witch Hazel
 - Harga: 120000
 - Rating: 4.2

...

Apakah kamu ingin mengetahui bagaimana cara menggunakannya? (ya/tidak): ya
Facewash:
1. Basahi wajah.
2. Aplikasikan facewash dan gosok lembut.
3. Bilas dengan air hangat dan keringkan dengan handuk lembut.
...
```

## Notes

- Ensure the server IP and port match between `client.py` and `server.py`.
- The Excel file must be correctly formatted to avoid errors.
- The system assumes the Excel file contains compatible data for the specified skin types and categories.
- Incompatible ingredient pairs are hardcoded in `server.py` and can be updated as needed.
