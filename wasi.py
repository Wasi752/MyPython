'''
a = int(input())
b = 0
while a > b:
    c = int(input())
    if c % 2 == 0:
        print('even')
    else:
        print('odd')
        
a = 1000
while a > 0:
    for x in range(0, 5):
        print(a, end='\t' )
        a = a - 1
    print('')
    
a = int(input())
b = 1
while b <= a:
    c = int(input())
    e = 1
    print("Case %d:" %b, end='')
    while e <= c:
        if c % e == 0:
            print(" %d" %e, end='')
        e = e + 1
    print('')
    a = a - 1
'''

    
