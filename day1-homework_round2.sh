#!/bin/bash
#
# Day 1 - Homework: Part 2 - debug this bash script
#
echo "There are around 6 mistakes"
FASTQ_DIR=/Users/cmdb/data/fastq
#need to move all 24 .gz files here
OUTPUT_DIR=/Users/cmdb/data/day1
#need to copy /Users/cmdb/data/day1-lunch/dmel-all-r5.57.gff to day1
FASTQ_FILE=SRR072
GENOME_DIR=/Users/cmdb/data/genomes
GENOME_INDEX=dmel-all-chromosome-r5.57
ANNOTATION=dmel-all-r5.57.gff
CORES=4
for i in {893..916}
  do echo fastqc $FASTQ_DIR/$FASTQ_FILE$i\.fastq.gz -o $OUTPUT_DIR
  echo tophat -p 4 -G $OUTPUT_DIR/$ANNOTATION -o $OUTPUT_DIR\.tophat.$FASTQ_FILE$i --no-novel-juncs --segment-length 20 $GENOME_DIR/$GENOME_INDEX $FASTQ_DIR$FASTQ_FILE$i\.fastq.gz
  echo cufflinks -p 4 -G $OUTPUT_DIR/$ANNOTATION -o $OUTPUT_DIR\.cufflinks.$FASTQ_FILE$i $OUTPUT_DIR\.tophat.$FASTQ_FILE$i/accepted_hits.bam
done