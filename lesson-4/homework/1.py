list1 = [1, 1, 2]
list2 = [2, 3, 4]

ans_list = []

for i in list1:
    if i in list2:
        continue
    ans_list.append(i)

for i in list2:
    if i in list1:
        continue
    ans_list.append(i)

print(ans_list)