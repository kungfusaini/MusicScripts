import random

output = ""

notes = ['Ab', 'A', 'A#',
         'Bb', 'B',
         'C', 'C#',
         'Db', 'D', 'D#',
         'Eb', 'E',
         'F', 'F#',
         'Gb', 'G', 'G#']

arpegg = ['Major 7th',
         'Minor 7th',
         'Dominant 7th',
         'Suspended 4th',
         'Major 6th',
         'Minor 6th']

output += 'Play: ' + (random.choice(notes)) + ' ' + (random.choice(arpegg) +' Arpeggio (1 Octave, 2 Positions)')

print()
print(output)
print()
