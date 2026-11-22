orders = [
    ["ORD-101", "Alice Smith", 120.50, 2, True, "USA", True],
    ["ORD-102", "Bob Jones", 2500.00, 1, False, "USA", False],
    ["ORD-103", "Charlie Brown", 45.00, 1, False, "Canada", True],
    ["ORD-104", "Diana Prince", 850.00, 6, True, "UK", True],
    ["ORD-105", "Evan Wright", 1200.00, 4, False, "Germany", True],
    ["ORD-106", "Fiona Glen", 35.00, 1, True, "USA", False],
    ["ORD-107", "George King", 3100.00, 8, False, "USA", True],
]

for var_item in orders:
    order_id, customer_name, order_amount, quantity, is_expedited, country, is_paid = var_item
    print(f"Order ID: {order_id}, Customer: {customer_name}, Amount: ${order_amount:.2f}, Quantity: {quantity}, Expedited: {is_expedited}, Country: {country}, Paid: {is_paid}"