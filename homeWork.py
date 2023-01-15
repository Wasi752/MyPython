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


