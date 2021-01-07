# Calculator using Functions with outputs
# 100 Days of Code - The Complete Python Pro Bootcamp for 2021 - Angela Yu Udemy Course

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

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]



# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
