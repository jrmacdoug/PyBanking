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

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.