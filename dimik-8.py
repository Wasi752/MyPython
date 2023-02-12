# ছোটো থেকে বড়ো
t = int(input())
i = 1
while i <= t:
    n = list(map(int, input().split()))
    n.sort()
    print("Case %d:" %i, end='')
    j = 0
    while j < len(n):
        print(" %d " %n[j], end='')
        j = j + 1
    print('')
    i = i + 1