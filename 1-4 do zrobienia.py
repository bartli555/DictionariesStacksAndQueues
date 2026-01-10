person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

for key, value in person.items():
    print(f"Klucz: {key}")
    print(f"Wartość: {value}")
    print(f"Typ wartości: {type(value).__name__}") # Wyświetla nazwę typu (np. 'int', 'list')
    print("-" * 20)