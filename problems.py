'''
print(1, 2, 3, 4, 5)
x = 1
while x < 501:
    print(x)
    x = x + 1

num = input()
reg = 0
while reg <= int(num):
    print(reg)
    reg = reg + 1

'''
a = input()
b = int(a)

while b > 0 :
    c = input()
    if len(c) < 11:
        print(c)
    else: 
        f = len(c)
        g = c[0]
        h = c[-1]
        j = f - 2
        print(g + str(j) + h)
    b = b - 1