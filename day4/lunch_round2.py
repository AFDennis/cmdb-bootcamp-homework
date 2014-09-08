#!/usr/bin/env python

import sys
import subprocess
import pandas
import matplotlib.pyplot as plot
import statsmodels.api as sm 
from fasta import FASTAReader
from pandas import DataFrame
import numpy         
reader = FASTAReader ( sys.stdin )              # pass file as stdin         

sid_out =[]
sequence_out = []
GCcontent= []
CpGisland = []
for sid, sequence in reader:
    sid_out.append(sid)
    sequence_out.append(sequence)
    #Calculate %GC content
    #got this from http://loris.som.jhmi.edu/python_course/examples.html
    G = sequence.count('G')
    C = sequence.count('C')
    GCcontent.append (float(G + C)/len(sequence))
    #Calculate % cpgisland content
    #more of the same
    GC = sequence.count('GC')
    CpGisland.append (float(GC)/len(sequence))

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


transcript_values = "/Users/cmdb/data/day4/day4-lunch/transcripts.gtf"
# counts the number of lines
f = open( transcript_values )

#need to extract FPKM values
FPKMvalues = []
FPKM = 'FPKM "'   
while True:
    line = f.readline()
    if not line:        # could just be if line == "":
        break           # allows us to exit the loop  
    elif line.find(FPKM) != -1:
        FPKMvalues.append(find_between(line, FPKM, '";'))

#put it in a table
FPKMvsGC = zip(FPKMvalues, GCcontent, CpGisland)

data = pandas.DataFrame(FPKMvsGC)
data.columns = ['FPKMvalues', 'GCcontent', 'CpGisland']

print data

model = sm.formula.ols(formula="FPKMvalues ~ GCcontent", data=data)

res = model.fit()

#print res.summary()

plot.scatter( data["FPKMvalues"], data["GCcontent"])

plot.savefig("FPKMvsGC.png")