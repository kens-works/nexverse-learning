# 1. Warehouse Inventory (Dictionary of Dictionaries)
inventory = {
    "P-101": {"name": "Wireless Mouse", "price": 25.00, "stock": 50},
    "P-102": {"name": "Mechanical Keyboard", "price": 85.00, "stock": 2},
    "P-103": {"name": "USB-C Hub", "price": 40.00, "stock": 0},
    "P-104": {"name": "Monitor Stand", "price": 30.00, "stock": 15}
}

# 2. Customer Profile
customer = {
    "customer_id": "CUST_8829",
    "name": "Alice Smith",
    "membership_tier": "VIP",  # Can be "VIP" or "Standard"
    "wallet_balance": 150.00
}

# 3. Shopping Cart (List of Dictionaries)
shopping_cart = [
    {"product_id": "P-101", "requested_qty": 1},
    {"product_id": "P-102", "requested_qty": 3},  # Note: Only 2 in stock!
    {"product_id": "P-103", "requested_qty": 1}   # Note: Out of stock completely!
]

#1. Stock Check (Read & Conditional)


#2. Adjust Orders & Inventory (Update)


#3. Calculate Costs & VIP Perks (Create & Operators)


#4. Warehouse Cleanup (Delete)

