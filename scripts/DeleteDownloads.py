#runninng this script will download all banking files in the Downloads folder and add them to the csv files

# First: it copies the files to archive folder
# Second: Copies files into the respective year csv file
# Third: Remove duplicates, sort the rows and saves the documents
from pathlib import Path
import os

# get the Download directory
Download_path = Path('C:/Users/jacob/Downloads')

#Copy over files
for f in Download_path.iterdir():
    if 'accountactivity' in str(f) or 'Transactions' in str(f):
        myfile=str(f)
        ## Try to delete the file ##
        try:
            os.remove(myfile)
        except OSError as e:  ## if failed, report it back to the user ##
            print ("Error: %s - %s." % (e.filename, e.strerror))