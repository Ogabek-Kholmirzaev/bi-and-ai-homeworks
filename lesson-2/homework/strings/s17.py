s = input()

vowels = "aeiouAEIOU"
res = ""

for char in s:
    if char in vowels:
        res += '*'
    else:
        res += char

print(res)