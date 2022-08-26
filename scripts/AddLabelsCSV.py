# this script will add all the labels to the CSV files where they are missing
# it will included pickled models that will help to predict them

import pandas as pd
import numpy as np

import csv
from pathlib import Path
from datetime import datetime

banking_path = Path.cwd()

message = """
Missing Label Found!:
  Description: {Description}
  Date: {Date}
  Amount: {Amount}
What is the Label?
  Label: """

def transact_update(ListOfPaths):
    for t in ListOfPaths:
        if datetime.now().year in str(t):
            with open(str(t),'r+') as f:
                reader = csv.reader(f)
                for r in reader:
                    try:
                        if r[-1] == '':     
                            new_transaction = r
                            new_transaction[-1] = input(message.format(Date=r[0],Description=r[1],Amount=r[2]))
                            print("Updated Transaction:",new_transaction)
                            with open(str(t),'a+') as f_writer:
                                writer = csv.writer(f_writer)
                                writer.writerow(new_transaction)
                    except IndexError:
                        pass
            
            #reindex and reorganize files
            t_csv = pd.read_csv(str(t),encoding='cp1252')
            t_csv = t_csv.sort_values(by=['TransactionDate','Label'], ascending=(True,True))        
            t_csv = t_csv.drop_duplicates(subset=t_csv.columns.difference(['Label']),keep='first')
            t_csv.reindex()
            with open(str(t),'w') as f:
                t_csv.to_csv(f
                        ,encoding='utf-8'
                        ,index=False
                        ,header=True
                        ,columns=['TransactionDate','Description','Amount','Debit?','Label']
                        ,line_terminator='\n'
                        )


# Run the label updater
transact_update(Path(banking_path,'data','csv','TD').iterdir())
transact_update(Path(banking_path,'data','csv','VISA').iterdir())
transact_update(Path(banking_path,'data','csv','MC').iterdir())
