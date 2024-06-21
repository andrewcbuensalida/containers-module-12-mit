To get started

## open docker desktop, and in command prompt, start the container
In command prompt,
  docker run -p 3307:3306 --name final_assignment -e MYSQL_ROOT_PASSWORD=MyNEWPass -d mysql
The -p 3307:3306 is needed because I already have a non-container mysql running on 3306. With -p 3307:3306, we are routing the container port 3306 to the local port 3307.

To start a redis container,
docker run -p 6379:6379 --name final_assignment_part3 -d redis


## Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment (mac/linux):

```bash
source .venv/bin/activate
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