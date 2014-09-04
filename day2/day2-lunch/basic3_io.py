#! /usr/bin/env python

cufflinks_output_fname = "/Users/cmdb/data/day2/day2-lunch/sam_short.sam"
# counts the number of lines
f = open( cufflinks_output_fname )

nl = 0 
while True:
    line = f.readline()
    if not line:        # could just be if line == "":
        break           # allows us to exit the loop  
    else:
        nl = nl + 1

singlecount = "NH:i:1"
field_single = 0 
field_multi = 0 
while True:
    line = f.readline()
    if not line:        # could just be if line == "":
        break           # allows us to exit the loop  
    elif line.find(singlecount) != -1:
        field_single = field_single + 1
    else:
        field_multi = field_multi + 1
        
print "Number of lines is ", nl
print "Number of single hits is ", field_single
print "Number of multihits is ", field_multi