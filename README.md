# Bakta_stats

**What is this script about?**

[Bakta](https://github.com/oschwengers/bakta) is a very nice tool for Bacterial genome annotation. However, if you used it for many genomes and you want to export the basic summary stats can be merged it a nice Excel sheet.


This simple Python3 script shall do this job.

If you have 1. the summary txt file in one folder and  these dependecies 

just type this command and you will get this nice excel sheet in the same folder.

```python
for file in *.fasta ; do seqtk sample -s185207 $file 185207  > sample_$file.fa ; done
```
