import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print("Dogs younger than 5 years:")
for dog in data:
    if dog["age"] < 5:
        print(f"Name: {dog['name']}, Age: {dog['age']}, Breed: {dog['breed']}")