string_list=list("Timur")
counter=0

tests=int(input())

for i in range(tests):
    string_len=int(input())
    spell_list=list(input())
    for i in range(len(spell_list)):
        if spell_list[i]=="T":
            counter=counter+1
        elif spell_list[i]=="i":
            counter=counter+2
        elif spell_list[i]=="m":
            counter=counter+3
        elif spell_list[i]=="u":
            counter=counter+4
        elif spell_list[i]=="r":
            counter=counter+5

        for x in range(len(spell_list)):
            if spell_list[i] not in string_list:
                counter=0

        if len(string_list) != len(set(spell_list)):
            counter=0

        if len(spell_list) != 5:
            counter=0

    if counter==15:           
        print("YES")
    else:
        print("NO")

    counter=0
