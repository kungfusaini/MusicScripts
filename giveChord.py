import random


root = ['Ab', 'A', 'A#',
        'Bb', 'B',
        'C', 'C#',
        'Db', 'D', 'D#',
        'Eb', 'E',
        'F', 'F#',
        'Gb', 'G', 'G#']

chord = ['',
         'm',
         'Maj6',
         'Maj7',
         'm6',
         'm7',
         '7',
         'sus4']

def generateChord():
        chosenRoot = random.choice(root)
        chosenChord = random.choice(chord)
        return chosenRoot+chosenChord

print()
#print('Play: ' + generateChord()+ ' (in 2 positions)')
print()

