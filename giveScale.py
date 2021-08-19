import random

output = ""

notes = ['Ab', 'A', 'A#',
         'Bb', 'B',
         'C', 'C#',
         'Db', 'D', 'D#',
         'Eb', 'E',
         'F', 'F#',
         'Gb', 'G', 'G#']

scale = ['Pentatonic Minor Scale - 1 Octave (5 Positions)',
         'Blues Scale - 1 Octave (5 Positions)',
         'Major Scale  - 1 Octave (3 Positions)',
         'Pentatonic Major Scale  - 2 Octave (3 Positions)',
         'Harmonic Minor - 2 Octave',
         'Pentatonic Minor Scale  - 1 Octave (In 5ths)']

output += 'Play: ' + (random.choice(notes)) + ' ' + (random.choice(scale))

print()
print(output)
print()
