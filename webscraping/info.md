
## Create a virtual env 

python -m venv ./venv

## Activate

### cmd.exe
venv\Scripts\activate.bat

### PowerShell
venv\Scripts\Activate.ps1

### MacOS and Linux
source venv/bin/activate


## Deactivate
deactivate


## “Freezing” Environment

pip freeze > requirements.txt


## Recreating Environment

pip install -r requirements.txt