#! /usr/bin/env python

#need to parse the script by > character again

#lets see what happens if we pass our blast output to the fasta parser

# need to get rid of sanity check in fasta reader 

import sys
import pandas as pd
from blast_big import BLASTReader


reader = BLASTReader ( sys.stdin )    

for sid, sequence in reader:
   print sid + "," + sequence[3]
   

#for _, sequence in reader:                          #this could be id, but since we dont use it later it doesn't have to be anything 
#    for i :          #want to stop 11 before the end
#        kmer = sequence[i:i+k]
#        if kmer not in kmers:
#            kmers[kmer] = set( [index] )              #put in index, set is similar to list, order doesn't matter, only knows it contains 1
#        else:
#            kmers[kmer].add( index )      #add element to set
#    index += 1

#print class1, class2


#looks like it worked
# now need to  print the sequence name, ratio of identifies, and ratio of gaps

#how do we search for these and print just the values?

#pass to pandas why not?




"""
while True:
    if line.stratrswith(">") or line.startswith("Query="):
        break
    elif line.strip().startswith(Identities):
"""
