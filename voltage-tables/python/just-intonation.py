# An example python script to create a voltage table for the ER-102.
# This table creates a just intonation scale by combining ratios
# generated from a set of (usually prime) integers.
import os
import ctypes

###################################
# Fill in these parameters
# the prime denominators to use to generate the ratios
denoms = [2,3,5,7]
# the name of this table, sets the filename and display name
name = "JUI7"
# the drive letter assigned to your mounted SD card
drive = "I:/"
###################################

# calculations
code_per_octave = 8000
max_code = 0xFFFF
nout = 100 
ratios = []

# iterate over each octave, appending new ratios as we go...
print "Generating 10 octaves of ratios using %s:"%str(denoms)
for octave in range(10):
    ratios.append(octave)
    # generate all possible ratios using the current denominator
    for d in denoms:
        for n in range(1,d):
            r = octave+(1.0*n)/d
            print "%d/%d = %f"%(n,d,r)
            ratios.append(r)

# sort the ratios into an increasing order
ratios.sort()
#print ratios

print "************************************"

# output to a binary file of 16-bit unsigned integers
filename = os.path.join(drive,"ER-102","TABLES",name+".BIN")
codes = [ int(code_per_octave * x) for x in ratios[:nout]]
codes = [ x if x<max_code else max_code for x in codes]
print "Outputting the following %d codes to %s:"%(len(codes),filename)
print codes
data = (ctypes.c_uint16 * len(codes))(*codes)
with open(filename,"wb") as f:
    f.write(data)
    f.close()
print "Done!"


