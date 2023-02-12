t = int(input())
i = 0
while i < t:
    str = input()
    ch = input()
    counter = 0
    for x in str:
        if x == ch:
            counter = counter + 1
    print(counter)
    i = i + 1