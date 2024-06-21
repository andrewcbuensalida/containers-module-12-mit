To get started

## Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment (mac/linux):

```bash
source .venv/Scripts/activate
```

For Windows
```bash
.venv\Scripts\activate.bat
```

In the future, to deactivate venv
```bash
.venv\Scripts\deactivate.bat 
```

## Install dependencies. This is not needed if doing a pip install in the notebook
pip install -r requirements.txt

## To save dependencies into requirements.txt
pip freeze > requirements.txt

## Sometimes imports could not be resolved
To fix, have to change the python interpreter to the one in .venv folder. Hover over squigly, quick fix, select a different interpreter, browse and choose the python.exe in .venv/Scripts