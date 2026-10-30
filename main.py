#data transformation

employees = [
    {"name": "John", "Salary": 500000, "bonus": 50000},
    {"name": "Mary", "Salary": 650000, "bonus": 75000},
    {"name": "Peter", "Salary": 400000, "bonus": 30000},
    {"name": "Anna", "Salary": 800000, "bonus": 100000}
]

new_salary = []
total_payroll = 0
for employee in employees:
    new_salary.append(employee["Salary"] + employee["bonus"])
    total_payroll += new_salary[-1]
    print(f"New salary for {employee['name']}: {new_salary[-1]}")
print(f"Total payroll: {total_payroll}")

#data extraction
inventory = [
    {"name": "Rice", "quantity": 25},
    {"name": "Sugar", "quantity": 4},
    {"name": "Cooking oil", "quantity": 2},
    {"name": "Beans", "quantity": 12},
    {"name": "Salt", "quantity": 5},
    {"name": "Flour", "quantity": 0}
]

restock_list = []
for product in inventory:
    if product["quantity"] <= 5:
        restock_list.append(product)

print(f"Products that need restock: {restock_list}")
print(f"Number of products: {len(restock_list)}")


#data cleaning
products = [
    {"name": "rice", "price":3000},
    {"name": "SUGAR", "price":2500},
    {"name": " Beans ", "price":-500},
    {"name": "cooking oil", "price":6500},
    {"name": "  ", "price":1000},
    {"name": "FLOUR", "price":0}
]

new_products = []
for product in products:
    cleaned_name = product["name"].strip().title()
    price = product["price"]

    if cleaned_name != "" and price > 0:
        new_products.append(product)
print(f"Valid products: {new_products}")



#COMAPARISON

customers = [

    {"name": "John", "email": "john@gmail.com"},
    {"name": "Mary", "email": ""},
    {"name": "Peter", "email": "None"},
    {"name": "Anna", "email": "anna@gmail.com"},
    {"name": "James", "email": ""}
]

valid_customers = []

for customer in customers:
    email = (customer["email"] or "").strip()
    is_valid = bool(email) and email.lower() != "none"

    print(f"{customer['name']}: {is_valid}")  # Boolean output

    if is_valid:
        valid_customers.append(customer)

print(f"Number of valid emails: {len(valid_customers)}")
 
        