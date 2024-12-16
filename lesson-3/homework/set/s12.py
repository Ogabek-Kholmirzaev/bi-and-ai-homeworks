my_set = set(map(int, input().split()))
element = int(input())

if element in my_set == False:
    my_set.add(element)

print("Set after Add:", my_set)