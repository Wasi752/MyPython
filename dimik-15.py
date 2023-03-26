t = int(input())
i = 0
while i < t:
    jumla = input()
    freq = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        freq[c] = 0
    for x in jumla:
        counter = 0
        for y in jumla:
            if y == x:
                counter = counter + 1
        if freq[x] == 0:
            freq[x] = 1
            print("{} = {}".format(x, counter))
    if i != t-1:
        print('')
    i = i + 1