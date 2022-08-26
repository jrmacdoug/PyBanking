#runninng this script will download all banking files in the Downloads folder and add them to the csv files

# First: it copies the files to archive folder
# Second: Copies files into the respective year csv file
# Third: Remove duplicates, sort the rows and saves the documents

import pandas as pd
import numpy as np 

import shutil
from pathlib import Path
from datetime import datetime

# get the Download directory
banking_path = Path.cwd()
csv_path = Path(banking_path,'CSV','TD-old')


for i in range(2017,2023):

    working_path = str(Path(csv_path,'TD-'+str(i)+'.csv'))

    tran_df = pd.read_csv(working_path)

    tran_df['Debit?'] = tran_df['Deposits'].apply(lambda d: not np.isnan(d))
    tran_df['Withdraws'] = tran_df['Withdraws'].fillna(0)
    tran_df['Deposits'] = tran_df['Deposits'].fillna(0)
    tran_df['Amount'] = tran_df['Withdraws'] + tran_df['Deposits']

    tran_df = tran_df.astype({'Year':str,'Month':str,'Day':str})
    tran_df['TransactionDate'] = tran_df['Year'] +'-'+ tran_df['Month'] +'-'+ tran_df['Day']
    tran_df['TransactionDate'] = pd.to_datetime(tran_df['TransactionDate'],format='%Y-%m-%d')


    print(tran_df.dtypes)
    print(tran_df)

    with open(working_path, 'w') as f:
        tran_df.to_csv(f
                ,encoding='utf-8'
                ,index=False
                ,header=True
                ,columns=['TransactionDate','Description','Amount','Debit?','Label']
                ,line_terminator='\n'
                )

