# Calculator using Functions with outputs
# 100 Days of Code - The Complete Python Pro Bootcamp for 2021 - Angela Yu Udemy Course
from time import sleep
from artwork import logo

# def format_name(fname, lname):
#     if fname == "" or lname == "":
#         return "You did not enter a name"
#     proper_fname = fname.title()
#     proper_lname = lname.title()
#     return f"Welcome, {proper_fname} {proper_lname}"
#
#
# print(format_name(input("What is your first name? \n"),
#                   input("What is your last name? \n")))


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid input"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
#
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Calculator

print(logo)
sleep(1)
print("Let's do some maths")
sleep(1)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Second number cannot be 0"
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}


num1 = int(input("What is the first number? \n"))
sleep(0.25)
for symbol in operators:
    print(symbol)
operator = input("Pick an operator from above. \n")
sleep(0.25)
num2 = int(input("What is the second number? \n"))

if operator == "+":
    answer = add(num1, num2)
elif operator == "-":
    answer = subtract(num1, num2)
elif operator == "*":
    answer = multiply(num1, num2)
else:
    answer = divide(num1, num2)

print(f"{num1} {operator} {num2} = {answer}")
