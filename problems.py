t = int(input())
i = 1
while i <= t:
    n = int(input())
    j = 1
    print("Case %d:" %i, end='')
    while j <= n:
        if n % j == 0:
            print(" %d" %j, end='')
        j = j + 1
    print('')
    i = i + 1

    '''
    input
    3
    10
    8
    6
    output
    2 4 6 8 10
    2 4 6 8
    2 4 6
    '''