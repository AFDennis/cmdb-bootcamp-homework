#! /usr/bin/env python

cufflinks_output_fname = "/Users/cmdb/data/day2/day2-lunch/accepted_hits.sam"
# counts the number of lines
f = open( cufflinks_output_fname )

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
print "The number of single hits is", field_single
print "The number of multiple hits is", field_multi

#/Users/cmdb/data/day2/day2-lunch $ ./basic3_io_2.py 
#The number of single hits is 17444391
#The number of multiple hits is 972797