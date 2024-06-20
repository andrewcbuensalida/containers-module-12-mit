When running python write.py, it errors with
- The C extension needed to use libev was not found.  This probably means that you didn't have the required build dependencies when installing the driver.  See http://datastax.github.io/python-driver/installation.html#c-extensions for instructions on installing build dependencies and building the C extension.
 - Unable to import asyncore module.  Note that this module has been removed in Python 3.12 so when using the driver with this version (or anything newer) you will need to use one of the other event loop implementations.

Try running that command on wsl?
- open wsl
- cd into :/mnt/c/swe/code/containers-module-12-mit/Activity 12.4 - Cassandra
- activate venv
- python3 write.py

Now the error is
  No module named 'cassandra'

Had to cd into .venv/Scripts then run python.exe ../../write.py
This produced the same error as running running python write.py in command prompt.

 - The C extension needed to use libev was not found.  This probably means that you didn't have the required build dependencies when installing the driver.  See http://datastax.github.io/python-driver/installation.html#c-extensions for instructions on installing build dependencies and building the C extension.
 - Unable to import asyncore module.  Note that this module has been removed in Python 3.12 so when using the driver with this version (or anything newer) you will need to use one of the other event loop implementations.

Now trying python version 3.11
- download from https://www.python.org/downloads/windows/

It works now
==========================================
To get started

## open docker desktop
In command prompt,
  docker run -p 9042:9042 --name some-cassandra -d cassandra

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