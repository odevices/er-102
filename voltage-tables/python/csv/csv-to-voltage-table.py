import ctypes
import csv
import sys
import getopt

def printHelp():
  print "This script converts a CSV file containing 2 columns (index and voltage) to the ER-102 voltage table format. Indices should extend from 0 to 99 and voltages should extend from 0 to 8.192.  The output file name should follow the format XXXX-P.BIN for tables that should be displayed as pitches by default, otherwise use XXXX.BIN."
  print
  print 'python csv-to-voltage-table.py -i <inputfile> -o <outputfile>'
  print
  print "EXAMPLE:"
  print "python csv-to-voltage-table.py -i test.csv -o TEST-P.BIN"
  print

def main(argv):
  inputfile = None
  outputfile = None
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    print 'csv-to-voltage-table.py -i <inputfile> -o <outputfile>'
    sys.exit(2)  
  for opt, arg in opts:
    if opt == '-h':
      printHelp()
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg

  if inputfile==None or outputfile==None:
    print "Error: no input or output file specified."
    print
    printHelp()
    sys.exit(2)
    
  # default voltage table
  voltages = [0]*100

  # parse the CSV file
  print "Reading:", inputfile
  count = 0
  with open(inputfile) as inputstream:
    reader = csv.DictReader(inputstream)
    for row in reader:
      # change field names to lower case
      row =  {k.lower(): v for k, v in row.items()}
      i = int(row["index"])
      v = float(row["voltage"])
      if i >= 0 and i < 100:
        count = count + 1
        voltages[i] = v
  print "Parsed",count,"entries."

  # output the voltage table as a flat binary array of unsigned shorts
  codes = [int(round(x*8000)) for x in voltages]
  # do not exceed the max for unsigned shorts
  codes = [x if x<(1<<16)-1 else (1<<16)-1 for x in codes]
  # convert the python list to a binary array
  table = (ctypes.c_uint16 * len(codes))(*codes)

  print "Writing:", outputfile
  with open(outputfile,"wb") as outputstream:
    outputstream.write(table)

if __name__ == "__main__":
   main(sys.argv[1:])
