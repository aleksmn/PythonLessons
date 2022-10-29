
## Create a virtual env 

python -m venv ./venv

## Activate
source venv/bin/activate


## “Freezing” Environment

pip freeze > requirements.txt


## Recreating Environment

pip install -r requirements.txt