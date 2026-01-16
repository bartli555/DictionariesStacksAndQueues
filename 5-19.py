import json

def get_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']

def count_rooms(reservations):
    return len(reservations)

def count_paid_unpaid(reservations):
    paid = 0
    unpaid = 0
    for res in reservations:
        if res['paid']:
            paid += 1
        else:
            unpaid += 1
    return paid, unpaid

def calculate_values(reservations):
    paid_value = 0
    unpaid_value = 0
    for res in reservations:
        amount = res['nights'] * res['price_per_night']
        if res['paid']:
            paid_value += amount
        else:
            unpaid_value += amount
    return paid_value, unpaid_value

# Main program execution
reservations = get_reservations('reservations.json')
num_rooms = count_rooms(reservations)
paid_count, unpaid_count = count_paid_unpaid(reservations)
paid_val, unpaid_val = calculate_values(reservations)

print("Hotel Reservation Summary")
print("=========================")
print(f"Number of rooms: {num_rooms}")
print(f"Paid reservations: {paid_count}")
print(f"Unpaid reservations: {unpaid_count}")
print(f"Total value of paid reservations: {paid_val:.2f}")
print(f"Total value of unpaid reservations: {unpaid_val:.2f}")