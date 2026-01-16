products = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

print("Lista produktów:")
for product, quantity in products.items():
    print(f"{product}: {quantity}")

total_quantity = sum(products.values())
print(f"Całkowita liczba produktów: {total_quantity}")