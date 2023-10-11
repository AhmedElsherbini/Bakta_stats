# Bakta_stats

**What is this script?**

[Bakta](https://github.com/oschwengers/bakta) is a very nice tool for bacterial genome annotation. However, if you used it for many genomes, and you want to merge the basic summary stats  into one Excel sheet, then this simple Python3 script shall do this job.


**What do you need?**

You shall have the summary.txt files in one folder and these dependencies (pandas, openpyxl ,and argparse)

Just type this command and you will get the Excel sheet in the same folder of your txt files.

"-i /--input_dir"  is your path to the directory of txt files 
"-p /--prefix"  is your prefered prefix for this work

```python
 python bakta_stats.py -i ./txt -p Corynebacterium
```

Thanks
