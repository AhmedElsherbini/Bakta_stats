# Bakta_stats

**What is this script?**

[Bakta](https://github.com/oschwengers/bakta) is a very nice tool for Bacterial genome annotation. However, if you used it for many genomes, and you want to merge the basic summary stats  into one Excel sheet.


This simple Python3 script shall do this job.

If you have the summary.txt files in one folder and these dependencies (pandas, numpy, openpyxl ,and argparse)

Just type this command and you will get this Excel sheet in the same folder of your txt files.

```python
 python bakta_stat.py -i ./txt
```
