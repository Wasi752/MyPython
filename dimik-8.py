# ছোটো থেকে বড়ো
'''
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
'''
t = int(input())
i = 1 
while i <= t:
    n1, n2, n3 = map(int, input().split()) # 3 2 1
    if n1 > n2:
        a = n1
        n1 = n2 
        n2 = a # 2 3 1
    if n2 > n3:
        a = n2
        n2 = n3
        n3 = a # 2, 1, 3  
    if n1 > n2:
        a = n1
        n1 = n2
        n2 = a # 1 2 3
    print("Case %d:" %i, end=' ')
    print( n1, n2, n3)
    i = i + 1     
