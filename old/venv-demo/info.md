
## Create a virtual env 

python -m venv .venv

## Activate
### Mac, Linux
source venv/bin/activate
### Windows
\venv\Scripts\activate

## “Freezing” Environment

pip freeze > requirements.txt


## Recreating Environment

pip install -r requirements.txt