def vectorsum():
    sum = 0
    cordlist = []
    newcordlist = []

    numoflines=int(input())

    for i in range(numoflines):
        coordinates=input()
        list(coordinates)
        cordlist.append(coordinates)

    cordstrings=' '.join(cordlist)

    cordlist=cordstrings.split(" ")

    for num in range(len(cordlist)):
        sum = sum + int(cordlist[num])

    if sum==0:
        return "YES"
    else:
        return "NO"

print(vectorsum())








