A_set = set(map(int, input().split()))
n = int(input())
is_superset = True

for i in range(n):
    other_set = set(map(int, input().split()))
    if not A_set.issuperset(other_set) or A_set == other_set:
        is_superset = False
        break

print(is_superset)
