'''
a = int(input())
b = 0
while a > b:
    c = input()
    last = c[-1]
    first = c[0]
    sum = (int(first) + int(last)) * len(c) / 2
    print(sum)
    a = a - 1
'''
a = int(input())
b = 1
counter = 0
while b <= a:
    c = input()
    for x in c:
        if int(x) % 2 == 0:
            counter = counter + 1
            i = counter
        else:
            counter = counter + 1
            y = counter 
    print("even = %d" %i, "odd = %d" %y)
    b = b + 1


