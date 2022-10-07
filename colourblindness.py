tests=int(input())
count=0

for test in range(tests):
    column=int(input())
    colour_row1=input()
    colour_row2=input()

    for i in range(column):
        if ((colour_row1[i] == "G" or colour_row1[i]== "B") and (colour_row2[i]=="G" or colour_row2[i]=="B")) or colour_row1[i]=="R" and colour_row2[i]=="R":
            count+=1
        
    if count==column:
        print("YES")
    else:
        print("NO")
    count=0

