'''
a = int(input())
b = 0
while a > b:
    c = input()
    last = c[-1]
    first = c[0]
    sum = (int(first) + int(last)) * len(c) // 2
    print(sum)
    a = a - 1

a = int(input())
b = 0
while a > b:
    counter = 0
    counter1 = 0
    c = input()
    for x in c:
        if int(x) % 2 == 0:
            counter = counter + 1
        else:
            counter1 = counter1 + 1
    print("even = %d," %counter, "odd = %d" %counter1)
    a = a - 1


input:
12345
234
17890
output:
15
9
25

a = int(input())
b = 1
while b <= a:
    c = int(input()) #5525
    sum = 0
    while c > 0:
        digit = c % 10
        sum = sum + digit
        c = c // 10
    print('Sum = %d' %sum)
    b = b + 1
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