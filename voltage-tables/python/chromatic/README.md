# Chromatic Scales for the ER-102

Execute the script using Python v2.x like this:

```bash
python2 generate.py
```

This will create many XXXX-P.BIN files where XXXX is a (shortened) name for the 4-character display of the ER-102.  The ```-P``` tells the ER-102 that these are pitch tables (as opposed to just voltage tables).

Here is the list of scales currently created by the script:

* Chro-P.BIN : Chromatic [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
* Majo-P.BIN : Major [0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 9, 11]
* Mino-P.BIN : Minor [0, 0, 2, 3, 3, 5, 5, 7, 7, 8, 10, 10]
* HMin-P.BIN : Harmonic Minor [0, 0, 2, 3, 3, 5, 5, 7, 7, 8, 11, 11]
* MMin-P.BIN : Melodic Minor [0, 0, 2, 3, 3, 5, 5, 7, 7, 9, 11, 11]
* Pent-P.BIN : Pentatonic [1, 1, 1, 3, 3, 6, 6, 6, 8, 8, 10, 10]
* PNeu-P.BIN : Pentatonic Neutral [0, 0, 2, 2, 2, 5, 5, 7, 7, 7, 10, 10]
* PMin-P.BIN : Pentatonic Minor [0, 0, 0, 3, 3, 5, 5, 7, 7, 7, 10, 10]
* PMaj-P.BIN : Pentatonic Major [0, 0, 2, 2, 4, 4, 4, 7, 7, 9, 9, 9]
* Blue-P.BIN : Blues [0, 0, 0, 3, 3, 5, 6, 7, 7, 7, 10, 10]
* Dori-P.BIN : Dorian [0, 0, 2, 3, 3, 5, 5, 7, 7, 9, 10, 10]
* Mixo-P.BIN : Mixolydian [0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 10, 10]
* Phry-P.BIN : Phrygian [0, 1, 1, 3, 3, 5, 5, 7, 8, 8, 10, 10]
* Lydi-P.BIN : Lydian [0, 0, 2, 2, 4, 4, 6, 7, 7, 9, 9, 11]
* Locr-P.BIN : Locrian [0, 1, 1, 3, 3, 5, 6, 6, 8, 8, 10, 10]
* DHal-P.BIN : Dim Half [0, 1, 1, 3, 4, 4, 6, 7, 7, 9, 10, 10]
* DWho-P.BIN : Dim Whole [0, 0, 2, 3, 3, 5, 6, 6, 8, 9, 9, 11]
* Augm-P.BIN : Augmented [0, 0, 0, 3, 4, 4, 6, 6, 8, 8, 8, 11]
* RMin-P.BIN : Roumanian Minor [0, 0, 2, 3, 3, 3, 6, 7, 7, 9, 10, 10]
* SGyp-P.BIN : Spanish Gypsy [0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 10, 10]
* Diat-P.BIN : Diatonic [0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 9, 9]
* DHar-P.BIN : Double Harmonic [0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 10]
* Eigh-P.BIN : Eight Tone Spanish [0, 1, 1, 3, 4, 5, 6, 6, 8, 8, 10, 10]
* Enig-P.BIN : Enigmatic [0, 1, 1, 1, 4, 4, 6, 6, 8, 8, 10, 11]
* Alge-P.BIN : Algerian [0, 0, 2, 3, 3, 5, 6, 7, 8, 8, 8, 11]
* AraA-P.BIN : Arabian A [0, 0, 2, 3, 3, 5, 6, 6, 8, 9, 9, 11]
* AraB-P.BIN : Arabian B [0, 0, 2, 2, 4, 5, 6, 6, 8, 8, 10, 10]
* Bali-P.BIN : Balinese [0, 1, 1, 3, 3, 3, 7, 8, 8, 8, 8, 8]
* Byza-P.BIN : Byzantine [0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 11]
* Chin-P.BIN : Chinese [0, 0, 0, 0, 4, 4, 6, 7, 7, 7, 7, 11]
* Egyp-P.BIN : Egyptian [0, 0, 2, 2, 2, 5, 5, 7, 7, 7, 10, 10]
* Hind-P.BIN : Hindu [0, 0, 2, 2, 4, 5, 5, 7, 8, 8, 10, 10]
* Hira-P.BIN : Hirajoshi [0, 0, 2, 3, 3, 3, 3, 7, 8, 8, 8, 8]
* HGyp-P.BIN : Hungarian Gypsy [0, 0, 2, 3, 3, 3, 6, 7, 8, 8, 8, 11]
* HPer-P.BIN : H.Gypsy Persian [0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 11]
* JapA-P.BIN : Japanese A [0, 1, 1, 1, 1, 5, 5, 7, 8, 8, 8, 8]
* JapB-P.BIN : Japanese B [0, 0, 2, 2, 2, 5, 5, 7, 8, 8, 8, 8]
* Pers-P.BIN : Persian [0, 1, 1, 1, 4, 5, 6, 6, 8, 8, 8, 11]
* Prom-P.BIN : Prometheus [0, 0, 2, 2, 4, 4, 6, 6, 6, 9, 10, 10]
* Six -P.BIN : Six Tone Symetrical [0, 1, 1, 1, 4, 5, 5, 5, 8, 9, 9, 9]
* SLoc-P.BIN : Super Locrian [0, 1, 1, 3, 4, 4, 6, 6, 8, 8, 10, 10]
* Whol-P.BIN : Wholetone [0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10]

All of these scales are quantizations of the base 12-TET scale.  In other words, each chromatic note is mapped to another note.  Often multiple notes are mapped to the same note.  This way you can write your song using modulo 12 scale degrees and then switch freely amongst any of these scales while preserving octave-equivalence.
