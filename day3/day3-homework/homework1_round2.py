#!/usr/bin/env python

#100 longest outputs from our cufflinks results -> gta to fasta before or after -> sort by length
#find open reading frames
#translate to amino acids

#transcript .gtf file

import sys
import subprocess
import pandas as pd
from fasta import FASTAReader
import numpy         
reader = FASTAReader ( sys.stdin )              # pass file as stdin         

sid_out =[]
sequence_out = []
alignments = []
for sid, sequence in reader:
    sid_out.append(sid)
    sequence_out.append(sequence)
    alignments.append(len(str(sequence)))

everything = zip(alignments, sid_out, sequence_out)

everything_sorted = sorted(everything, reverse = True)

top = everything_sorted[0:100]

#now to read open reading frames
#i got this from the internet http://stackoverflow.com/questions/19570800/reverse-complement-dna
#need to get reverse compliment
def complement(s): 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters)
def revcom(s):
    complement(s[::-1])
    return complement(s[::-1])
   

(alignments, sid_out, sequence_out) = zip(*top)
   
#print (alignments, sid_out, sequence_out)

rc = []

for things in sequence_out:
    rc.append(revcom(things))
        
#need to iterate over 3 frames
#lets define everything
Frame1F = sequence_out
Frame2F = []
Frame3F = []

Frame1R = rc
Frame2R = []
Frame3R = []

#now we gotta fill these in
    #use frame1 = sequence[1:]
    #use frame2 = sequence[2:]
    
for things in sequence_out:
    Frame2F.append(things[1:])
    Frame3F.append(things[2:])
    
for things in rc:
    Frame2R.append(things[1:])
    Frame3R.append(things[2:])
    

#need to pass codons
#MOdify kmers code to get words of 3
k = 3

codons = []                  #creates blank dictionairy
#need to make a dictionary of kmers(11 nucleotide long strings) and count how many times we see them
#need to cut between start and stop codon


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

for sequence in Frame1F:                          #this could be id, but since we dont use it later it doesn't have to be anything 
    index = 0
    fill=""
    
    for index in range( index, len(sequence) - k):          #want to stop 3 before the end, ,3 should iterate by 3s
        codon = sequence[(index*3):(index*3+k)]
        fill += codon + ' '
        index += 1
        
    fill_end = fill.replace("TAG", "END")
    fill_end = fill.replace("TAA", "END")
    fill_end = fill.replace("TGA", "END")
    
    
    fill_cut= find_between( fill_end, 'ATG', 'END')
    fill_cut = 'ATG ' + fill_cut 
    codons.append(''.join(fill_cut)) 
      
    
    # substituttion
    
#this still doesn't work 

AAseq = []

def translate(s): 
    AAtrans = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L", "TCT":"S", "TCC":"s", "TCA":"S", "TCG":"S","TAT":"Y", "TAC":"Y", "TAA":"STOP", "TAG":"STOP","TGT":"C", "TGC":"C", "TGA":"STOP", "TGG":"W","CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L","CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P","CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q","CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R","ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M","ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T","AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K","AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R","GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V","GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A","GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E","GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    letters = list(s)
    letters = [AAtrans[base] for base in letters] 
    return ''.join(letters)

for things in codons:
    AAseq.append(translate(things))

print AAseq

print Frame1F
print codons
print codons_trans
        
#print index of start codon
    

#need to recognize start codon (ATG)
#need to recognize stop codon (TAG, TAA, or TGA)
