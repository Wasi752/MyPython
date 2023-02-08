
'''
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
    
     # Home Work 28-1-23
  
t = int(input())
i = 0
while t > i:
    n = int(input())
    j = 0
    k = "*"
    while j < n:
        print(k.rjust(25))
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
    while j < n:
        print(k.center(25))
        j = j + 1
        k = k + "*" + "*"
    t = t - 1
