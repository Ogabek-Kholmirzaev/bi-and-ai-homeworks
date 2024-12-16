set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

disjoint = set1.isdisjoint(set2)

if len(disjoint) == 0:
    print(True)
else:
    print(False)