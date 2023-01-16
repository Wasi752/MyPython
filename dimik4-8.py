#  প্রোগ্রামিং সমস্যা ৭ — সংখ্যা গণনা  
t = int(input())
i = 0
while t > i:
    n = input()
    j = 0
    num = ""
    counter = 0
    while j < len(n):
        if n[j] != " ":
            num = num + n[j]
        else:
            counter = counter + 1
            num = ""
        j = j + 1
    counter = counter + 1
    print(counter)
    i = i + 1

