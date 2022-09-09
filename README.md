# PyBanking

PyBanking is a group of Python scripts I use to keep track of my personal banking. It is specific to my credit card statements (both from TD bank and the Canadian Tire Mastercard), and thus may not be applicable right out of the box.

## Installation

Create a git clone repository, make a new venv environment in your local folder, and install the requirements.txt file:

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt 
```

## Usage

First, I donwload the CSV files from my accounts. The scripts assume they download to the local Downloads folder for the User.

Then, I run the `_GetDownloads.bat` to move the files to my local folder and combine them with the existing CSV files I have.

The batch file will organize them all, point out any transactions without labels (which I have always manually added myself), and delete the Downloaded CSV files.

I then use Jupyter notebooks to inspect the CSV files.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.