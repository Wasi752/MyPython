
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



