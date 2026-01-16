prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}
cart = {'juice': 3, 'bread': 1, 'milk': 2}

total_cost = 0.0

for item, quantity in cart.items():
    if item in prices:
        cost = prices[item] * quantity
        total_cost += cost

print(f"Total cost: {total_cost:.2f}")