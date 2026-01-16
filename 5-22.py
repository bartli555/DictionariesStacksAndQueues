import json

print("--- Product Data Entry ---")

# Read product data from keyboard
product = {}

# Name (String)
product["name"] = input("Enter product name: ")

# Price (Float, 2 decimal places)
try:
    price_input = input("Enter price: ").replace(',', '.') # Allow comma as separator
    product["price"] = round(float(price_input), 2)
except ValueError:
    print("Invalid price format. Setting to 0.00")
    product["price"] = 0.00

# Paid status (Boolean)
paid_input = input("Has it been paid? (yes/no): ").lower()
product["paid"] = (paid_input == "yes" or paid_input == "y")

# Save product data to json file
file_name = "product.json"

try:
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(product, file, indent=4)
    print(f"\nProduct saved to {file_name}")
    
    # Optional: Print content to verify
    print("Saved content:", json.dumps(product, indent=4))
    
except IOError:
    print("Error saving file.")