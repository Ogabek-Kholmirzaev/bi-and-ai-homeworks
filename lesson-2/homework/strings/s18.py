s = input("input = ")
starts_with_s = input("start with = ")
ends_with_s = input("ends with = ")

if s.startswith(starts_with_s) and s.endswith(ends_with_s):
    print("yes")
else:
    print("no")