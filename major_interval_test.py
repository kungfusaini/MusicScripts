import random


major_steps = [2,2,1,2,2,2]

natural_notes = ['C', 'D','E','F', 'G', 'A','B']

possibleKeys = ['C', 'Db', 'D','Eb', 'E','F', 'F#', 'G','Ab', 'A','Bb', 'B']

notes = ['C', ('C#','Db'), 'D', ('D#','Eb'), 'E','F', ('F#','Gb'), 'G', ('G#','Ab'), 'A', ('A#','Bb'), 'B']

sharpKeys = ['G','D','A','E','B','F#']

flatKeys = ['F','Bb','Eb','Ab','Db','Gb']

intervalMap = {2: "Major Second", 3:"Major Third", 4:"Perfect Fourth", 5:"Perfect Fifth", 6:"Major Sixth", 7:"Major Seventh"}

def indexCounter(current, toMove):
    last = len(notes) - 1
    temp = current + toMove
    if(temp > last):
        temp = (temp%last) - 1
    return temp


def randomMajorScale():
    output = ""
    sharpKey = True
    root = random.choice(possibleKeys)
    tupleIndex = 0

    if(root in flatKeys): sharpKey = False 
    if(not sharpKey): tupleIndex = 1
    
    i = possibleKeys.index(root)
    output += root + " "

    for step in major_steps:
        i = indexCounter(i,step)
        temp = notes[i]
        if (type(temp) is tuple):
            temp = temp[tupleIndex]
        output += temp + " "

    return output

def randomInterval():
    majorScale = randomMajorScale().split(" ")
    intervalChoice = random.randint(2,7)
    interval = intervalMap.get(intervalChoice)
    print("What is the {} in the key of {} Major?".format(interval,majorScale[0]))
    input("")
    print(majorScale[intervalChoice - 1])



while True:
    randomInterval()
    print("")
    print("")