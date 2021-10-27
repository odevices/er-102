# Chromatic Scales for the ER-102

```bash
python2 generate.py
```

The chromatic/generate.py script generates the following scales:

* Chro : Chromatic [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
* Majo : Major [0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 9, 11]
* Mino : Minor [0, 0, 2, 3, 3, 5, 5, 7, 7, 8, 10, 10]
* HMin : Harmonic Minor [0, 0, 2, 3, 3, 5, 5, 7, 7, 8, 11, 11]
* MMin : Melodic Minor [0, 0, 2, 3, 3, 5, 5, 7, 7, 9, 11, 11]
* Pent : Pentatonic [1, 1, 1, 3, 3, 6, 6, 6, 8, 8, 10, 10]
* PNeu : Pentatonic Neutral [0, 0, 2, 2, 2, 5, 5, 7, 7, 7, 10, 10]
* PMin : Pentatonic Minor [0, 0, 0, 3, 3, 5, 5, 7, 7, 7, 10, 10]
* PMaj : Pentatonic Major [0, 0, 2, 2, 4, 4, 4, 7, 7, 9, 9, 9]
* Blue : Blues [0, 0, 0, 3, 3, 5, 6, 7, 7, 7, 10, 10]
* Dori : Dorian [0, 0, 2, 3, 3, 5, 5, 7, 7, 9, 10, 10]
* Mixo : Mixolydian [0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 10, 10]
* Phry : Phrygian [0, 1, 1, 3, 3, 5, 5, 7, 8, 8, 10, 10]
* Lydi : Lydian [0, 0, 2, 2, 4, 4, 6, 7, 7, 9, 9, 11]
* Locr : Locrian [0, 1, 1, 3, 3, 5, 6, 6, 8, 8, 10, 10]
* DHal : Dim Half [0, 1, 1, 3, 4, 4, 6, 7, 7, 9, 10, 10]
* DWho : Dim Whole [0, 0, 2, 3, 3, 5, 6, 6, 8, 9, 9, 11]
* Augm : Augmented [0, 0, 0, 3, 4, 4, 6, 6, 8, 8, 8, 11]
* RMin : Roumanian Minor [0, 0, 2, 3, 3, 3, 6, 7, 7, 9, 10, 10]
* SGyp : Spanish Gypsy [0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 10, 10]
* Diat : Diatonic [0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 9, 9]
* DHar : Double Harmonic [0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 10]
* Eigh : Eight Tone Spanish [0, 1, 1, 3, 4, 5, 6, 6, 8, 8, 10, 10]
* Enig : Enigmatic [0, 1, 1, 1, 4, 4, 6, 6, 8, 8, 10, 11]
* Alge : Algerian [0, 0, 2, 3, 3, 5, 6, 7, 8, 8, 8, 11]
* AraA : Arabian A [0, 0, 2, 3, 3, 5, 6, 6, 8, 9, 9, 11]
* AraB : Arabian B [0, 0, 2, 2, 4, 5, 6, 6, 8, 8, 10, 10]
* Bali : Balinese [0, 1, 1, 3, 3, 3, 7, 8, 8, 8, 8, 8]
* Byza : Byzantine [0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 11]
* Chin : Chinese [0, 0, 0, 0, 4, 4, 6, 7, 7, 7, 7, 11]
* Egyp : Egyptian [0, 0, 2, 2, 2, 5, 5, 7, 7, 7, 10, 10]
* Hind : Hindu [0, 0, 2, 2, 4, 5, 5, 7, 8, 8, 10, 10]
* Hira : Hirajoshi [0, 0, 2, 3, 3, 3, 3, 7, 8, 8, 8, 8]
* HGyp : Hungarian Gypsy [0, 0, 2, 3, 3, 3, 6, 7, 8, 8, 8, 11]
* HPer : H.Gypsy Persian [0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 11]
* JapA : Japanese A [0, 1, 1, 1, 1, 5, 5, 7, 8, 8, 8, 8]
* JapB : Japanese B [0, 0, 2, 2, 2, 5, 5, 7, 8, 8, 8, 8]
* Pers : Persian [0, 1, 1, 1, 4, 5, 6, 6, 8, 8, 8, 11]
* Prom : Prometheus [0, 0, 2, 2, 4, 4, 6, 6, 6, 9, 10, 10]
* Six  : Six Tone Symetrical [0, 1, 1, 1, 4, 5, 5, 5, 8, 9, 9, 9]
* SLoc : Super Locrian [0, 1, 1, 3, 4, 4, 6, 6, 8, 8, 10, 10]
* Whol : Wholetone [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10]


All of these scales are quantizations of the base 12-TET scale.  In other words, each chromatic note is mapped to another note.  Often multiple notes are mapped to the same note.  This way you can write your song using modulo 12 scale degrees and then switch freely amongst any of these scales while preserving octave-equivalence.