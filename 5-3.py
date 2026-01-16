# Translations
translations = {
    "computer": "komputer",
    "mouse": "myszka",
    "keyboard": "klawiatura",
    "printer": "drukarka"
}

word = input("Enter word in English: ")
if word in translations:
    print(f"PL: {translations[word]}")
else:
    print("Word unavailable")