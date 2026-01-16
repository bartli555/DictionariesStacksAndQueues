basic_data = {
   "name": "Barbara",
   "age": 21
}

advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

# Tworzymy słownik 'person' kopiując 'basic_data'
person = basic_data.copy()

# Aktualizujemy go danymi z 'advanced_data'
person.update(advanced_data)

print("Person dictionary content:")
print(person)