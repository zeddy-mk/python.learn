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
    #print(f"New salary for {employee['name']}: {new_salary[-1]}")
#print(f"Total payroll: {total_payroll}")

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

#print(f"Products that need restock: {restock_list}")
#print(f"Number of products: {len(restock_list)}")


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
#print(f"Valid products: {new_products}")



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

employees = [
    {"name": "John", "Salary": 1500000},
    {"name": "Mary", "Salary": 800000},
    {"name": "Peter", "Salary": 500000},
    {"name": "Anna", "Salary": 2000000},
    {"name": "James", "Salary": 300000}
]

employee_statuses = []

for employee in employees:
    salary = employee["Salary"]

    if salary > 1_000_000:
        status = "High Performer"
    elif salary == 500_000:
        status = "Target Achieved"
    elif salary < 500_000:
        status = "Lower Performer"
    else:
        status = "Average Performer"

    employee_statuses.append(f"{employee['name']} Status: {status}")

print(employee_statuses)



payments = [
    {"customer": "John", "amount": 50000},
    {"customer": "Mary", "amount": "75000"},
    {"customer": "Peter", "amount": 30000.5},
    {"customer": "Anna", "amount": None},
    {"customer": "James", "amount": 100000}
]
valid_numeric_amounts = 0
payment_results = []
for payment in payments:
    status = "Valid" if isinstance(payment["amount"], (int, float)) else "Invalid"
    payment_results.append(f"{payment['customer']} Payment: {status}")

print(payment_results)

print(f"Number of records with valid numeric amounts: {valid_numeric_amounts}")



      #PYTHON LOGIC OPERATORS 

# Check if a user's name is not empty and the age is greater than or equal to 18
user_name = "Alice"
user_age = 20
is_adult = 18

valid_user = user_name != "" and user_age >= is_adult
print(f"Is the user valid: {valid_user}")


#Check if the password is at least 8 characters long and does not contain spaces
password = " mypassword"
valid_pasword = len(password) >= 8 and " " not in password
print(f"Is the password valid: {valid_pasword}")


# Check if a user's email is not  empty, contains '@', and ends with '.com'
user_email = "mk@gmail.om"
valid_email = user_email != "" and "@" in user_email and user_email.endswith(".com")
print(f"Is the email valid: {valid_email}")


# Check if username is a string, is not None, and is longer the 5 characters
user_name = "John"
valid_username = isinstance(user_name, str) and user_name is not None and len(user_name) > 5
print(f"Is the username valid: {valid_username}")

#Check if the user is either an admin or moderator, and either they're not banned or they've verified their email.
user_role = "admin"
user_role2 = "moderator"
is_banned = False
email_verified = True
valid_user_role = (user_role == "admin" or user_role2 == "moderator") and (not is_banned or email_verified)
print(f"Is the user role valid: {valid_user_role}")






                         #IF, ELIF, ELSE STATEMENTS#

# 1.Validate the quality and correctness of Email values.
# Must not be empty
# Must contain '@' and '.'
# Must contain exactly one '@' symbol
# Must end with 'com', '.org', or 'net'
# Must not be longer than 254 characters
# Must start and end with a letter or digit






# 2.Validate the quality and correctness of Password values.
# Must not be empty
# Must be at least 8 characters long
# Must include at least 1 uppercase
# Must include at least 1 lowercase
# Must not be the same as the email
# Must not contain any spaces
# Must start and end with a letter or digit