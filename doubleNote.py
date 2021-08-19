import random

output = ""

notes = ['Ab', 'A', 'A#',
         'Bb', 'B',
         'C', 'C#',
         'Db', 'D', 'D#',
         'Eb', 'E',
         'F', 'F#',
         'Gb', 'G', 'G#']

output += 'Notes: (' + (random.choice(notes)) + ',' + (random.choice(notes)) + ')'

print()
print(output)
print()

