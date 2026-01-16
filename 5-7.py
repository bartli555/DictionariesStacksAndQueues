hotels_in_Krakow = [
   {"name": "Sky", "price": 320.00},
   {"name": "Metropol", "price": 480.00},
   {"name": "New Port", "price": 420.00},
   {"name": "Aparthotel", "price": 390.00}
]

hotels_in_Sopot = [
   {"name": "Focus", "price": 510.00},
   {"name": "Aqua", "price": 345.00},
   {"name": "La Boutique", "price": 390.00},
   {"name": "Marina", "price": 410.00}
]

def hotel_list(hotels):
    names = [h["name"] for h in hotels]
    return ", ".join(names)

def avg_price(hotels):
    total = sum(h["price"] for h in hotels)
    return round(total / len(hotels))

avg_krakow = avg_price(hotels_in_Krakow)
avg_sopot = avg_price(hotels_in_Sopot)

print(f"Hotels in Krakow: {hotel_list(hotels_in_Krakow)}")
print(f"Average hotel price in Krakow: {avg_krakow}")

print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
print(f"Average hotel price in Sopot: {avg_sopot}")

if avg_krakow < avg_sopot:
    print("Cheaper hotels in: Krakow")
else:
    print("Cheaper hotels in: Sopot")