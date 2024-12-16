my_set = set(map(int, input().split()))
element = int(input())

if element in my_set:
    my_set.remove(element)

print(my_set)