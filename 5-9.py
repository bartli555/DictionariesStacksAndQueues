import csv

provinces = {}
province_file = 'province.csv'
vehicle_file = 'vehicle.txt'

#Wczytanie województw
try:
    with open(province_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Zakładamy format: Litera,Województwo
        for row in reader:
            if len(row) >= 2:
                provinces[row[0]] = row[1]
except FileNotFoundError:
    provinces = {'K': 'Małopolskie', 'W': 'Mazowieckie', 'G': 'Pomorskie'} 

#Zliczanie pojazdów
vehicle_counts = {province: 0 for province in provinces.values()}

try:
    with open(vehicle_file, 'r', encoding='utf-8') as file:
        for line in file:
            plate = line.strip()
            if plate:
                first_letter = plate[0]
                if first_letter in provinces:
                    province_name = provinces[first_letter]
                    vehicle_counts[province_name] += 1
except FileNotFoundError:
    print(f"Error: File {vehicle_file} not found.")

print("Registered vehicles by province:")
for province, count in vehicle_counts.items():
    print(f"{province}: {count}")