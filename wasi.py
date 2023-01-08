
a = int(input())
b = 1
while b <= a:
    c = int(input())
    d = 1
    print("Case %d:" %b, end='')
    while d <= c:
        if c % d == 0:
            print(" %d" %d, end='')
        d = d + 1
    print('')
    b = b + 1
    