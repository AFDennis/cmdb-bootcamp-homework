#! /usr/bin/env python

cufflinks_output_fname = "/Users/cmdb/data/day2/day2-lunch/accepted_hits.sam"
# counts the number of lines
f = open( cufflinks_output_fname )

nl = 0 
while True:
    line = f.readline()
    if not line:        # could just be if line == "":
        break           # allows us to exit the loop  
    else:
        nl = nl + 1
print "The number of lines is", nl 

#./basic1_io.py 
#The number of lines is 18417195