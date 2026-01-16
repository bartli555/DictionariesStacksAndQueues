import queue

customer_queue = queue.Queue()

# Customers arrive
customer_queue.put("Ticket #101")
customer_queue.put("Ticket #102")
customer_queue.put("Ticket #103")

print("Serving customers:")
while not customer_queue.empty():
    current_customer = customer_queue.get()
    print(f"Now serving: {current_customer}")