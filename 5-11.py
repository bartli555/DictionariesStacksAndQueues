import json

file_name = 'vote.json'

print("--- System Głosowania ---")

#Odczyt zawartości pliku JSON
try:
    # Otwieramy plik do odczytu
    with open(file_name, 'r', encoding='utf-8') as file:
        votes = json.load(file)
except FileNotFoundError:
    # Jeśli plik nie istnieje, tworzymy pusty słownik
    votes = {}

#Głosowanie na osobę
person_name = input('Name of the person you are voting for: ').strip()

if person_name:
    #Zwiększamy liczbę głosów lub dodajemy nową osobę
    if person_name in votes:
        votes[person_name] += 1
    else:
        votes[person_name] = 1

    #Zapis danych do pliku JSON
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(votes, file, indent=4)
        print(f"Vote registered for {person_name}. Current votes: {votes[person_name]}")
    except IOError:
        print("Error saving vote data.")
else:
    print("No name entered. Vote cancelled.")

#Wyświetlenie aktualnego stanu głosowania
print("\nCurrent Standings:")
for candidate, count in votes.items():
    print(f"- {candidate}: {count}")