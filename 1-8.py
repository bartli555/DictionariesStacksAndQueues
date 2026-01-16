price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("Ceny przed rabatem:")
for item, price in price_list.items():
    print(f"{item}: {price:.2f}")

total_before = sum(price_list.values())
print(f"Suma przed rabatem: {total_before:.2f}")

# Obniżka o 10%
for item in price_list:
    price_list[item] = round(price_list[item] * 0.90, 2)

print("\nCeny po rabacie:")
for item, price in price_list.items():
    print(f"{item}: {price:.2f}")

total_after = sum(price_list.values())
print(f"Suma po rabacie: {total_after:.2f}")