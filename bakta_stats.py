#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 12:18:10 2023

@author: ahmed_elsherbini
"""
###########################################
import argparse
import pandas as pd
import numpy as np
import os
import openpyxl

###########################################
my_parser = argparse.ArgumentParser(description='Welcome!')
print("example: $ python bakta_stat.py -i ./txt")



my_parser.add_argument('-i','--input_dir',
                       action='store',
                        metavar='input_dir',
                       type=str,
                       help="input_dir")

###########################################
# Execute the parse_args() method
args = my_parser.parse_args()

###########################################
diro  = args.input_dir
diro = "/media/ahmed/CC69-620B6/00_Ph.D/DATA_results/0_accolens_prop_database_work/0_analysis/00_bakta/txt_files"
os.chdir(diro)
file_names = os.listdir()

###########################################

    
data_frames = []
for file_name in file_names:
    if file_name.endswith(".txt"):
        df = pd.read_csv(file_name, sep=":")
        # Add filename as new column
        df["filename"] = file_name
        # Append data frame to list
        data_frames.append(df)
        
        
head = data_frames[0].iloc[:, 0]

df2 = head.to_frame(name="Isolate")

df2 = df2.T


for data_frame in data_frames:
        # Append data frame to list
        isolate = data_frame.iloc[:,2][0]
        isolate = pd.Series(isolate)
        raw = data_frame.iloc[:, 1]
        new_raw = pd.concat([isolate,raw], ignore_index=True)
        new_raw = new_raw.to_frame(name=new_raw[0])
        new_raw = new_raw.T
        new_raw.drop(new_raw.columns[[0]], axis=1, inplace=True)
        new_raw = new_raw.rename(columns={x:y for x,y in zip(new_raw.columns,range(0,len(new_raw.columns)))})
        df2 = pd.concat([df2,new_raw])
        


#df2.drop(new_raw.columns[6], axis=1, inplace=True)
df2.drop(new_raw.columns[6], axis=1, inplace=True)
df2.drop(new_raw.columns[22:27], axis=1, inplace=True)
###########################################
df2.to_excel('Bakta_stats.xlsx', index=True , header=False)
###########################################