import datetime

name = input("name = ")
birth_year = int(input("birth year = "))

print(f"{name} is {datetime.datetime.now().year - birth_year} years old")