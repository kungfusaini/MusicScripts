from giveChord import generateChord


while (True):
    output = ""
    for x in range(1, 11):
        output += generateChord()
        if(x % 10 != 0):
            output += ", "
            

    print("")
    print(output)
    print("")
    input("")