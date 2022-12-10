attend, noOfhighestMark = map(int, input().split())
marksList = list(map(int, input().split()))
marksList.sort(reverse=True)
mark = marksList[noOfhighestMark - 1]
counter = 0
for x in marksList:
    if mark <= x and x > 0:
        counter = counter + 1
print(counter)

