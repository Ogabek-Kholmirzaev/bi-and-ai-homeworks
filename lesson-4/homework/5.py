password = input()

has_less_8_characters = len(password) < 8
no_uppercase = True

for i in password:
    if i.isupper():
        no_uppercase = False
        break

if has_less_8_characters:
    print("Password is too short.")
if no_uppercase:
    print("Password must contain an uppercase letter.")
if has_less_8_characters == False and no_uppercase == False:
    print("Password is strong.")