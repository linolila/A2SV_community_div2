# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_count = int(input())
eng_roll = set(input().split())
fre_count = int(input())
fre_roll = set(input().split())
both_eng_fre = len(eng_roll.union(fre_roll))
print(both_eng_fre)
