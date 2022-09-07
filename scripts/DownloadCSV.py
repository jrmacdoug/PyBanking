#runninng this script will download all banking files in the Downloads folder and add them to the csv files

# First: it copies the files to archive folder
# Second: Copies files into the respective year csv file
# Third: Remove duplicates, sort the rows and saves the documents

from configparser import ConverterMapping
import pandas as pd
import numpy as np 

import shutil
from pathlib import Path
from datetime import datetime

# get the Download directory
download_path = Path('C:/Users/jacob/Downloads')
banking_path = Path.cwd()
data_path = Path(banking_path,'data')

# Archive directory
archive_path = Path(data_path,'csv','archive',datetime.today().strftime('%Y-%m-%d'))

#Create an archive folder
if not Path(banking_path,archive_path).exists():
    Path(banking_path,archive_path).mkdir(parents=True)

#Copy over files
for f in download_path.iterdir():
    if 'accountactivity' in str(f) or 'Transactions' in str(f):
        shutil.copyfile(str(f),str(Path(archive_path,f.name)))

#function to combine given pandas DF with any CSV in the folder
# takes a dataframe and a directory and adds the dataframe into the correct files respectively by year
def combine_year(download_df,folder_Str):
    min_y = min(download_df['TransactionDate'].dt.year)
    max_y = max(download_df['TransactionDate'].dt.year)
    for i in range(min_y,max_y+1):
        i_fname = Path(data_path,'csv',folder_Str,folder_Str+'-'+str(i)+'.csv')

        i_df = pd.read_csv(i_fname,encoding='cp1252')
        d_df = download_df[download_df['TransactionDate'].dt.year == i]

        i_df['TransactionDate'] = pd.to_datetime(i_df['TransactionDate'],format='%Y-%m-%d')
        d_df['TransactionDate'] = pd.to_datetime(d_df['TransactionDate'],format='%Y-%m-%d')
        print('  ',folder_Str,'\n',d_df)

        combined_df = pd.concat([i_df,d_df],ignore_index=True)
        combined_df = combined_df.drop_duplicates(subset=combined_df.columns.difference(['Label']),keep='first')
        combined_df = combined_df.sort_values(by=['TransactionDate'], ascending=(True))        
        combined_df.reindex()

        with open(i_fname, 'w') as file:
            combined_df.to_csv(file
                    ,encoding='utf-8'
                    ,index=False
                    ,header=True
                    ,columns=['TransactionDate','Description','Amount','Debit?','Label']
                    ,line_terminator='\n'
                    )


for a in archive_path.iterdir():
    #for VISA and TD csv files
    if 'accountactivity' in str(a):
        #open folder
        TD_download = pd.read_csv(str(a)
            ,names=['Date','Description','Credit','Debit','Balance'])
            
        #add columns
        TD_download['TransactionDate'] = pd.to_datetime(TD_download['Date'])
        TD_download['Debit?'] = TD_download['Debit'].apply(lambda d: not np.isnan(d))
        TD_download['Amount'] = TD_download['Credit'].replace(np.nan,0) + TD_download['Debit'].replace(np.nan,0)
        TD_download['Label'] = ''

        #re-organize columns
        TD_download = TD_download.reindex(['TransactionDate','Description','Amount','Debit?','Label'], axis=1)
        
        #combine with CSV folder
        if 'accountactivity (' in str(a):
            combine_year(TD_download,'VISA')
        elif 'accountactivity.csv' in str(a):
            combine_year(TD_download,'TD')
    
    #for mastercard file
    if 'Transactions' in str(a):
        #open file
        MC_download = pd.read_csv(str(a)
            ,skiprows=4
            ,names=['RefNum','Date','Posted_Date','Type','Description','Category','Amount'])

        #add in missing years        
        MC_download['TransactionDate'] = pd.to_datetime(MC_download['Date'])
        MC_download['Debit?'] = np.where(MC_download['Type']=='PAYMENT',True,False)
        MC_download['Label'] = ''

        #re-organize columns
        MC_download = MC_download.reindex(['TransactionDate','Description','Amount','Debit?','Label'], axis=1)

        combine_year(MC_download,'MC')



