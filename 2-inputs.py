import datetime as DT

def get_date(string):
    year,month,day = string.split("/")
    date = DT.datetime(year,month,day)
    return date

first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")
family_name = input("Enter your family name: ")
full_name = f"{first_name} {second_name} {family_name}"
print("---------------------")
age = int(input("Enter your age: "))
print("---------------------")
birthday = input("Enter your birth day: ")
birth_date = get_date(birthday)
# show infos
print(f"Full name: {full_name}")
print(f"Age: {age}")
print(f"birth_day: {birth_date.year}/{birth_date.month}/{birth_date.day}")