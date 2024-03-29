# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
list1 = []
d = defaultdict(list)
n , m = map(int,input().split())
for i in range(n):
   a = input()
   d[a].append(i+1)
for i in range(m): 
   b = input()
   list1 = list1 + [b]
for i in list1:
    if i in d:
        print(" ".join(map(str,d[i])))
    else:
        print(-1)



