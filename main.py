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

email = "id.2@.net"
if email == "":
    print("Email must not be Empty!")

elif not('.' in email and '@' in email):
    print("Email must contain . and @")

elif email.count('@') != 1:
    print("Email must contain one @ symbol")

elif not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com, .org, or .net")

elif len(email) > 254:
    print("Email must not be longer than 254 characters")

elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")

else:
    print("Email is Valid")








# 2.Validate the quality and correctness of Password values.
# Must not be empty
# Must be at least 8 characters long
# Must include at least 1 uppercase
# Must include at least 1 lowercase
# Must not be the same as the email
# Must not contain any spaces
# Must start and end with a letter or digit

password = "i@.nSSDAEt"
email = "id.2@.net"

if password == "":
    print("Password must not be Empty!")

elif len(password) < 8:
    print("Password must be at least 8 characters long")

elif not any(character.isupper() for character in password):
    print("Password must include at least 1 uppercase letter")

elif not any(character.islower() for character in password):
    print("Password must include at least 1 lowercase letter")

elif password == email:
    print("Password must not be the same as the email")

elif password.count(" ") > 0:
    print("Password must not contain any spaces")

elif not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")

else:
    print("Password is Valid")



                 #Conditional statements and Loops

    #task one


employees = [
    {"name": "John", "salary": 1500000, "score": 95},
    {"name": "Mary", "salary": 800000, "score": 70},
    {"name": "Peter", "salary": 500000, "score": 60},
    {"name": "Anna", "salary": 2000000, "score": 97},
    {"name": "James", "salary": 300000, "score": 59},
    {"name": "David", "salary": 1200000, "score": 90},
    {"name": "Sarah", "salary": 900000, "score": 75}
]

print("Name | Score | Bonus | Final Salary")
print("-" * 55)

for employee in employees:

    # Determine bonus rate using performance score
    if employee["score"] >= 90:
        bonus_rate = 0.20
    elif employee["score"] >= 75:
        bonus_rate = 0.15
    elif employee["score"] >= 60:
        bonus_rate = 0.10
    else:
        bonus_rate = 0.00

    # Calculate bonus and final salary
    bonus_amount = employee["salary"] * bonus_rate
    final_salary = employee["salary"] + bonus_amount

    # Store calculated values for later use
    employee["bonus_amount"] = bonus_amount
    employee["final_salary"] = final_salary

    print(
        f"{employee['name']:<10} | "
        f"{employee['score']:<5} | "
        f"{bonus_amount:,.2f} | "
        f"{final_salary:,.2f}"
        )
        
        

print("-" * 55)

# Total employees
print(f"Number of employees: {len(employees)}")

# Total bonuses
total_bonus_paid = sum(
    employee["bonus_amount"] for employee in employees
)

print(f"Total bonuses paid: TZS {total_bonus_paid:,.2f}")

# Employee with highest final salary
highest_employee = max(
    employees,
    key=lambda x: x["final_salary"]
)

print(
    f"Highest paid employee: {highest_employee['name']} "
    f"- TZS {highest_employee['final_salary']:,.2f}"
    )








  #2task two


products = [
    {"name": "Rice", "price": 300000, "quantity": 25},
    {"name": "Sugar", "price": 250000, "quantity": 4},
    {"name": "Cooking oil", "price": 65000, "quantity": 2},
    {"name": "Beans", "price": 50000, "quantity": 12},
    {"name": "Salt", "price": 15000, "quantity": 5},
    {"name": "Flour", "price": 20000, "quantity": 0},
    {"name": "Pasta", "price": 400000, "quantity": 8},
    {"name": "Tomato sauce", "price": 3500, "quantity": 0}
]

total_supermarket_sales = 0
total_customers = 1

for customer in range(1, total_customers + 1):

    print(f"\nCUSTOMER {customer}")
    print("-" * 50)

    receipt_items = []

    # Process customer purchases
    for product in products:

        requested_quantity = int(
            input(f"How many {product['name']} would you like to buy? ")
        )

        if requested_quantity <= 0:
            print("Please enter a quantity greater than 0.")
            continue

        if requested_quantity > product["quantity"]:
            print(
                f"Purchase rejected: Only "
                f"{product['quantity']} available."
            )
            continue

        # Calculate purchase subtotal
        subtotal = product["price"] * requested_quantity

        # Determine discount based on subtotal
        if subtotal >= 200000:
            discount_rate = 0.15
        elif subtotal >= 100000:
            discount_rate = 0.10
        elif subtotal >= 50000:
            discount_rate = 0.05
        else:
            discount_rate = 0.00

        # Calculate discount and final amount
        discount = subtotal * discount_rate
        final_amount = subtotal - discount

        # Update available stock
        product["quantity"] -= requested_quantity

        # Save purchase information
        receipt_items.append({
            "name": product["name"],
            "quantity": requested_quantity,
            "unit_price": product["price"],
            "subtotal": subtotal,
            "discount": discount,
            "total": final_amount
        })

    # Generate customer receipt
    print("\nCUSTOMER RECEIPT")
    print("-" * 75)

    print(
        f"{'Item':<18}{'Qty':>5}{'Price':>12}"
        f"{'Subtotal':>14}{'Discount':>12}{'Total':>14}"
    )

    customer_subtotal = sum(item["subtotal"] for item in receipt_items)
    customer_discount = sum(item["discount"] for item in receipt_items)
    customer_total = sum(item["total"] for item in receipt_items)

    for item in receipt_items:
        print(
            f"{item['name']:<18}"
            f"{item['quantity']:>5}"
            f"{item['unit_price']:>12,.0f}"
            f"{item['subtotal']:>14,.0f}"
            f"{item['discount']:>12,.0f}"
            f"{item['total']:>14,.0f}"
        )

    print("-" * 75)
    print(f"Subtotal: TZS {customer_subtotal:,.2f}")
    print(f"Discount: TZS {customer_discount:,.2f}")
    print(f"Final amount: TZS {customer_total:,.2f}")

    total_supermarket_sales += customer_total

# Supermarket summary
print("\nSUPERMARKET DAILY SUMMARY")
print("-" * 40)
print(f"Customers served: {total_customers}")
print(f"Total sales: TZS {total_supermarket_sales:,.2f}")

print("\nREMAINING STOCK")
print("-" * 40)

for product in products:
    print(f"{product['name']}: {product['quantity']} remaining")




                     #CONTROL STATEMENTS



# Task 1: Attendance Recording
attendance = [
    "Present",
    "Present",
    "Absent",
    "Present",
    "Absent",
    "Stop",
    "Stop",
    "Present",
    "Absent"
]

for status in attendance:
    if status == "Stop":
        print("Attendance recording stopped.")
        break

    if status == "Absent":
        print("Student is absent.")
        continue

    print("Student is present.")




#Task 2 Bank Transaction Monitoring

transactions = [
    50000,
    -2000,
    75000,
    0,
    120000,
    -5000,
    90000,
    0,
    150000,
    30000
]

for transaction in transactions:
    if transaction <= 0:
        continue

    if transaction > 100000:
        print("Transaction exceeds 100,000. Processing stopped.")
        break

    print(f"Processed Transaction: {transaction:,.2f}.")
    






                         #PYTHON FOR ELSE LOOPS

products = [
    {"name": "Rice", "price": 3000, "quantity": 20},
    {"name": "Sugar", "price": 2500, "quantity": 10},
    {"name": "Beans", "price": 4000, "quantity": 5},
    {"name": "Cooking Oil", "price": 6500, "quantity": 8},
    {"name": "Flour", "price": 2000, "quantity": 15}
]

total_amount = 0

for product in products:
    requested_quantity = int(
        input(f"How many {product['name']} would you like to buy? ")
    )

    if requested_quantity == 999:
        print("Purchase cancelled by user.")
        break

    if requested_quantity <= 0:
        print("Please enter a quantity greater than 0.")
        continue

    if requested_quantity > product["quantity"]:
        print(
            f"Purchase rejected: Only "
            f"{product['quantity']} available."
        )
        continue

    subtotal = product["price"] * requested_quantity
    total_amount += subtotal
    product["quantity"] -= requested_quantity
    print(f"Subtotal for {product['name']}: TZS {subtotal:,.2f}")

print(f"\nTotal for all valid purchases: TZS {total_amount:,.2f}")

print("\nREMAINING STOCK")
for product in products:
    print(f"{product['name']}: {product['quantity']} remaining")














                         #PYTHON NESTED LOOPS