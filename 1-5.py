countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 67000000},
    {"name": "Spain", "population": 47000000},
    {"name": "Italy", "population": 60000000}
]

print("COUNTRY  POPULATION")
for country in countries:
    print(f"{country['name']:8} {country['population']}")