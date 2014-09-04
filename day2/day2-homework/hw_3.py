#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axis as ax

#read in all the files
cufflinks_f10 = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
cufflinks_f11 = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
cufflinks_f12 = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
cufflinks_f13 = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
cufflinks_f14A = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
cufflinks_f14B = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
cufflinks_f14C = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
cufflinks_f14D = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

#make everything a dataframe
df_f10 = pd.read_table(cufflinks_f10)
df_f11 = pd.read_table(cufflinks_f11)
df_f12 = pd.read_table(cufflinks_f12)
df_f13 = pd.read_table(cufflinks_f13)
df_f14A = pd.read_table(cufflinks_f14A)
df_f14B = pd.read_table(cufflinks_f14B)
df_f14C = pd.read_table(cufflinks_f14C)
df_f14D = pd.read_table(cufflinks_f14D)

"""
trying store all the names of the variables to run a loop with. 
There is probably a more elegent way of doing this, but I couldn't figure out how to use just the name of the dataframe as a string
tried something like: thing['File'] = "%s" % (thing) 
"""

index = [(df_f10,'df_f10'), (df_f11, 'df_11'), (df_f12, 'df_f12'), (df_f13, 'df_13'), (df_f14A, 'df_f14A'), (df_f14B, 'df_f14B'), (df_f14C, 'df_f14C'), (df_f14D, 'df_f14D')]

#Add a column to the dataframe to specify which development stage it was taken at
for thing, name in index:
    thing['File'] = name

#need to store all the names of the variables again, this time as a regular list
females = (df_f10, df_f11, df_f12, df_f13, df_f14A, df_f14B, df_f14C, df_f14D)

#putting all the data together
bigdata = females[0].append(list(females[1:8]))

#lets save this to a file for tomorrow
#bigdata.to_csv("Female_FPKM.csv", index = False) 

#now it's time to pull out just the Sxl entries
bigdata_subset = bigdata[ bigdata['gene_short_name'] == "Sxl"]    

#lets pull out just the columns we need in a better order   
small = bigdata_subset[['File', 'gene_short_name', 'FPKM']]

#save to file
#small.to_csv("Female_Sxl_FPKM.csv", index = False)   

#this again
names = ('df_f10', 'df_f11', 'df_f12', 'df_f13', 'df_f14A', 'df_f14B', 'df_f14C', 'df_f14D')

#now lets plot
plt.figure()
fig, ax = plt.subplots()
plt.title('mRNA Abundance Over Different Female Developmental Stages')
plt.xlabel('Developmental Stage')
plt.ylabel('mRNA abundance')
ax.set_xticklabels(names)
plt.plot( small['FPKM'])
plt.savefig("line.png")

    