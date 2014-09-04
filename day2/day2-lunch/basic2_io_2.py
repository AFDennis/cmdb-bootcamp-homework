#! /usr/bin/env python

cufflinks_output_fname = "/Users/cmdb/data/day2/day2-lunch/accepted_hits.sam"
# counts the number of lines
f = open( cufflinks_output_fname )

perfect = "NM:i:0"
field_perfect = 0 
while True:
    line = f.readline()
    if not line:        # could just be if line == "":
        break           # allows us to exit the loop  
    elif line.find(perfect) != -1:
        field_perfect = field_perfect + 1
print "The number of perfect hits is", field_perfect


#/Users/cmdb/data/day2/day2-lunch $ ./basic2_io_2.py 
#The number of perfect hits is 14079052

