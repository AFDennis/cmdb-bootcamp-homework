#!/bin/bash
#
# Day 1 - Homework: Part 2 - debug this bash script
#
echo "There are around 6 mistakes"
FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
GENOME_DIR=/Users/cmdb/data/genomes
SAMPLE_PREFIX=dmel5
ANNOTATION=dmel-all-r5.57.gff
CORES=4
for i in 893*
  do echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  echo tophat 
  echo cufflinks
done

  ## this script runs for all 24 rna data sets it will echo out the what the commands would be, to run this delete all the echos