#! /usr/bin/env python

#need to parse the script by > character again

#lets see what happens if we pass our blast output to the fasta parser

# need to get rid of sanity check in fasta reader 

import sys
import pandas as pd
from blast_out import FASTAReader
from blast_out_2 import BLASTReader
        
reader = FASTAReader ( sys.stdin )              # pass file as stdin  

reader2 = BLASTReader ( sys.stdin )    

for sid, sequence in reader:
   print sid
   print sequence[3]
   

sys.stdin.seek(0,0)

for flyid, summarys in reader2:
    print flyid

table 


#print class1, class2


#looks like it worked
# now need to  print the sequence name, ratio of identifies, and ratio of gaps

#how do we search for these and print just the values?

#pass to pandas why not?





