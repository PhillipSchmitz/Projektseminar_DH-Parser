#====imports====
import pandas as pd
import re
import numpy as np
from xml.etree import ElementTree as ET
import glob

#====parameters====
input_folder = "sql_sagen/csv"


#====functions====

def read_csv(filepath):
    with open(filepath, "r", encoding="utf8") as infile: 
        dataframe = pd.read_csv(infile, sep=";")
    return dataframe

def save_data(df, filename):
    with open(filename, "w", encoding="utf8") as outfile: 
        df.to_csv(outfile, sep=";", lineterminator='\n')
    print("Formated Data CSV created")

n=0
for filename in glob.glob(input_folder + '/*.csv'):
    data = read_csv(filename)
    if n==0:
        master_csv = data
    else:
        master_csv = pd.concat([data, master_csv], axis=0)
    n+=1
    print(n)


master_csv.set_index('sagenid', inplace=True)
master_csv.sort_index(axis=0)
print(master_csv)
save_data(master_csv, "Master_csv.csv")

#coord_csv = master_csv
#print (coord_csv)
for index, row in master_csv.iterrows():
    #print(index)
    if row['longitude'] == 0.0 or row['longitude'] == '' or row['longitude'] == 'NaN' or pd.isnull(row['longitude']):
        master_csv.drop(index, inplace=True)
    else:
        if len(row['volltext']) > 1000:
            master_csv.loc[index, 'volltext'] = str(row['volltext'][:1000] + '<a href="https://mosel-sagen.de/einzelansicht-sagen/?markerid=' + str(index) + '">[...]</a>')
            #master_csv.loc[index, 'volltext'] = row['volltext'][:1000]
        master_csv.loc[index, 'werkid'] = int(row['werkid'])
        master_csv.loc[index, 'sagenidimwerk'] = int(row['sagenidimwerk'])
save_data(master_csv, "Master_csv_with_coord.csv")

