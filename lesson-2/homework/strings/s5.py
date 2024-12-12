vowels = "aeiouAEIOU"

s = input()

vowels_count = 0
consonants_count = 0

for char in s:
    if char in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print(f"vowels count = {vowels_count}, consonants count = {consonants_count}")