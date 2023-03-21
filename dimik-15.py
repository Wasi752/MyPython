t = int(input())
i = 0
while i < t:
    jumla = input()
    ch = "abcdefghijklmnopqrstuvwxyz"
    for x in ch:
        counter = 0
        for y in jumla:
            if x == y:
                counter = counter + 1
        if counter != 0:
            print("{} = {}".format(x, counter))
    print('')
    i = i + 1
