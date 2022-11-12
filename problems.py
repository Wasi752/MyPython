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
'''
a = input()
b = int(a)
counter = 0
while ( b > 0):
  g = input() 
  h,i,j = g.split()
  l = int(h), int(i), int(j)
  h,i,j = l
  if (h + i + j > 1):
    counter = counter + 1
  b = b -1
print(counter)