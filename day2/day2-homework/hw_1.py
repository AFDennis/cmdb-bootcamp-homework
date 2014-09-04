#! /usr/bin/env python
#lets get all our libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#define data locations
cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

#make data frames
df = pd.read_table( cufflinks_output )
df2 = pd.read_table( cufflinks_output2 )

#define percentiles
df_33 = np.percentile(df["FPKM"], 33.33333333333)
df_66 = np.percentile(df["FPKM"], 66.66666666666)

#subset our data in 3 by percentile cuttoffs
df_low = df[ df["FPKM"] <= df_33]                                                                # return low 30th percentile
df_mid = df[ (df["FPKM"] > df_33) & (df["FPKM"] <= df_66)]                                     # return mid 30th percentile
df_top = df[ df["FPKM"] > df_66]                                                                # return top 30th percentile

#do it again for data2
df2_33 = np.percentile(df2["FPKM"], 33.33333333333)
df2_66 = np.percentile(df2["FPKM"], 66.66666666666)

#do it again for data2
df2_low = df2[ df2["FPKM"] <= df2_33]                                                                # return low 30th percentile
df2_mid = df2[ (df2["FPKM"] > df2_33) & (df2["FPKM"] <= df2_66)]                                     # return mid 30th percentile
df2_top = df2[ df2["FPKM"] > df2_66]                                                                # return top 30th percentile

#put all the data frames in a list to plot
data_to_plot = [df_low['FPKM'].values, df_mid['FPKM'].values, df_top['FPKM'].values, df2_low['FPKM'].values, df2_mid['FPKM'].values, 

#make new dataframe with only FPKM values
df2_top['FPKM'].values]
#this should work too: data_to_plot = [df_low['FPKM'], df_mid['FPKM'], df_top['FPKM'], df2_low['FPKM'], df2_mid['FPKM'], df2_top['FPKM']] #make new dataframe with only 

#let's plot
fig = plt.figure()
fig, ax = plt.subplots()
plt.boxplot(data_to_plot)
plt.ylim(-100,1000)
plt.title('Summary FPKM values for Male and Female')
ax.set_xticklabels(['Male low', 'Male mid', 'Male top', 'Female low', 'Female mid', 'Female top'])
plt.savefig("box.png")

