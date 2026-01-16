import json
import urllib.request  # Biblioteka standardowa do łączenia się z internetem

# Adres API NBP (Tabela C, Euro, ostatnie 10 notowań)
url = "http://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json"
file_name = "euro.json"

print("--- Pobieranie kursów walut (Euro) z NBP ---")

try:
    # 1. Pobieranie danych z Internetu (Prawdziwe połączenie)
    print(f"Łączenie z {url}...")
    with urllib.request.urlopen(url) as response:
        # Odczytujemy dane i dekodujemy z bajtów na tekst
        json_text = response.read().decode('utf-8')
        # Zamieniamy tekst na słownik Pythona
        data = json.loads(json_text)
    
    # 2. Zapisywanie pobranych danych do pliku euro.json
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
        
    print(f"Sukces! Dane zostały zapisane do pliku '{file_name}'.\n")

except Exception as e:
    print(f"Błąd podczas pobierania danych: {e}")
    # Jeśli wystąpi błąd (np. brak internetu), program zakończy działanie w tym punkcie
    exit()

# 3. Odczyt z pliku i wyświetlanie tabeli
print(f"{'Date':12} {'Buying Rate':15} {'Selling Rate':15}")
print("=" * 45)

try:
    with open(file_name, 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
        
        # Sprawdzamy czy klucz 'rates' istnieje w danych
        if "rates" in loaded_data:
            for rate in loaded_data["rates"]:
                date = rate["effectiveDate"]
                bid = rate["bid"]  # Kurs kupna
                ask = rate["ask"]  # Kurs sprzedaży
                
                # Formatowanie tabeli
                print(f"{date:12} {bid:<15.4f} {ask:<15.4f}")
        else:
            print("Pobrane dane mają nieprawidłowy format.")

except FileNotFoundError:
    print("Błąd: Plik nie istnieje.")