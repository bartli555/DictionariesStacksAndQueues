import json

# Dictionary describing a favorite book
favorite_book = {
    "title": "The Witcher: The Last Wish",
    "author": "Andrzej Sapkowski",
    "genre": "Fantasy",
    "year_published": 1993,
    "rating": 9.5,
    "main_characters": ["Geralt", "Yennefer", "Dandelion"]
}

file_name = "favorite.json"

# Save dictionary to JSON file
try:
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(favorite_book, file, indent=4)
    print(f"Data has been saved to {file_name}")
except IOError:
    print("Error saving file.")