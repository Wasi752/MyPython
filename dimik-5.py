'''
t = int(input())
i = 0
while t > i:
    x = int(input())
    j = 0
    while j < x:
        k = 0
        while k < x:
            print("*", end='')
            k = k + 1
        print("")
        j = j + 1
    print('')
    i = i + 1

t = int(input())
i = 0
while t > i:
    n = int(input())
    j = 0
    k = "*"
    while j < n:
        print(k)
        j = j + 1
        k = k + "*"
    t = t - 1
'''
t = int(input())
i = 0
while t > i:
    n = int(input())
    j = 0
    k = "*"
    while n > j:
        print(k * n)
        n = n - 1
    t = t - 1