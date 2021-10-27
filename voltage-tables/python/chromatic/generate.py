# This Python script converts the scales given in text format below
# to the ER-102's voltage table format.

import ctypes

# The following scales were provided by EAT@dnp-music
input_data = """
Chromatic: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Major: 0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 9, 11
Minor: 0, 0, 2, 3, 3, 5, 5, 7, 7, 8, 10, 10
Harmonic Minor: 0, 0, 2, 3, 3, 5, 5, 7, 7, 8, 11, 11
Melodic Minor: 0, 0, 2, 3, 3, 5, 5, 7, 7, 9, 11, 11
Pentatonic: 1, 1, 1, 3, 3, 6, 6, 6, 8, 8, 10, 10
Pentatonic Neutral: 0, 0, 2, 2, 2, 5, 5, 7, 7, 7, 10, 10
Pentatonic Minor: 0, 0, 0, 3, 3, 5, 5, 7, 7, 7, 10, 10
Pentatonic Major: 0, 0, 2, 2, 4, 4, 4, 7, 7, 9, 9, 9
Blues: 0, 0, 0, 3, 3, 5, 6, 7, 7, 7, 10, 10
Dorian: 0, 0, 2, 3, 3, 5, 5, 7, 7, 9, 10, 10
Mixolydian: 0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 10, 10
Phrygian: 0, 1, 1, 3, 3, 5, 5, 7, 8, 8, 10, 10
Lydian: 0, 0, 2, 2, 4, 4, 6, 7, 7, 9, 9, 11
Locrian: 0, 1, 1, 3, 3, 5, 6, 6, 8, 8, 10, 10
Dim Half: 0, 1, 1, 3, 4, 4, 6, 7, 7, 9, 10, 10
Dim Whole: 0, 0, 2, 3, 3, 5, 6, 6, 8, 9, 9, 11
Augmented: 0, 0, 0, 3, 4, 4, 6, 6, 8, 8, 8, 11
Roumanian Minor: 0, 0, 2, 3, 3, 3, 6, 7, 7, 9, 10, 10
Spanish Gypsy: 0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 10, 10
Diatonic: 0, 0, 2, 2, 4, 5, 5, 7, 7, 9, 9, 9
Double Harmonic: 0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 10
Eight Tone Spanish: 0, 1, 1, 3, 4, 5, 6, 6, 8, 8, 10, 10
Enigmatic: 0, 1, 1, 1, 4, 4, 6, 6, 8, 8, 10, 11
Algerian: 0, 0, 2, 3, 3, 5, 6, 7, 8, 8, 8, 11
Arabian A: 0, 0, 2, 3, 3, 5, 6, 6, 8, 9, 9, 11
Arabian B: 0, 0, 2, 2, 4, 5, 6, 6, 8, 8, 10, 10
Balinese: 0, 1, 1, 3, 3, 3, 7, 8, 8, 8, 8, 8
Byzantine: 0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 11
Chinese: 0, 0, 0, 0, 4, 4, 6, 7, 7, 7, 7, 11
Egyptian: 0, 0, 2, 2, 2, 5, 5, 7, 7, 7, 10, 10
Hindu: 0, 0, 2, 2, 4, 5, 5, 7, 8, 8, 10, 10
Hirajoshi: 0, 0, 2, 3, 3, 3, 3, 7, 8, 8, 8, 8
Hungarian Gypsy: 0, 0, 2, 3, 3, 3, 6, 7, 8, 8, 8, 11
H.Gypsy Persian: 0, 1, 1, 1, 4, 5, 5, 7, 8, 8, 8, 11
Japanese A: 0, 1, 1, 1, 1, 5, 5, 7, 8, 8, 8, 8
Japanese B: 0, 0, 2, 2, 2, 5, 5, 7, 8, 8, 8, 8
Persian: 0, 1, 1, 1, 4, 5, 6, 6, 8, 8, 8, 11
Prometheus: 0, 0, 2, 2, 4, 4, 6, 6, 6, 9, 10, 10
Six Tone Symetrical: 0, 1, 1, 1, 4, 5, 5, 5, 8, 9, 9, 9
Super Locrian: 0, 1, 1, 3, 4, 4, 6, 6, 8, 8, 10, 10
Wholetone: 0, 0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10
"""

def abbreviate(x):
    """
    A small routine to automatically derive an abbreviation from the long name.
    """
    try:
        first,last = x.split(' ')
        if len(last)>2:
            return "%s%s"%(first[0],last[0:3])
        elif len(last)==1:
            return "%s%s"%(first[0:3],last[0])
        else:
            return first[0:4]
    except:
        return x[0:4]

def chromatic_to_voltage_table(degrees):
    """
    Convert a list of chromatic scale degrees to a binary voltage table.
    """
    # roll out the degrees to 100 entries
    unrolled = [degrees[i%len(degrees)]+12*(i/12) for i in range(100)]
    # create a list of codes for each semitone
    codes = [int(round(x*8000/12.0)) for x in unrolled]
    # do not exceed the max for unsigned shorts
    codes = [x if x<(1<<16)-1 else (1<<16)-1 for x in codes]
    # convert the python list to a binary array
    table = (ctypes.c_uint16 * len(codes))(*codes)
    return table

# parse the input data, line by line
for item in input_data.split('\n'):
    if len(item)==0: continue
    scale = item.split(':')
    scale_name = scale[0]
    scale_degrees = [int(x) for x in scale[1].split(',')]
    scale_short_name = abbreviate(scale_name)
    filename = scale_short_name+"-P.BIN"
    print "*", filename, ":", scale_name, scale_degrees
    table = chromatic_to_voltage_table(scale_degrees)
    # Write the binary array out to a binary file.
    # Note: The '-P' at the end of the filename indicates a pitched table and thus voltages
    #       will be shown as note values rather than numeric values.
    with open(filename,"wb") as f:
        f.write(table)
        f.close()
    
