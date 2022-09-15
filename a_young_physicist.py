noflines=int(input("How many set of coordinates?: "))
cordlist=[]
sum=0

for set in range(noflines):
    x = int(input("Enter x "))
    cordlist.append(x)
    y = int(input("Enter y "))
    cordlist.append(y)
    z = int(input("Enter z "))
    cordlist.append(z)
    print()

for num in range(len(cordlist)):
    sum=sum+cordlist[num]

if sum==0:
    print("YES")
else:
    print("NO")







