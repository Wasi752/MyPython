a = int(input())
counter = 0
while a > 0:
    b = input()
    if (b[1] == "+"):
        counter = counter + 1
    else:
        counter = counter - 1
    a = a - 1
print(counter)