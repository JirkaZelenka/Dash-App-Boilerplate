# Dash-App-Boilerplate
This boilerplate should allow for easy setup of a dash app, with several pages, navbar, suggested components as database manager, etc.

|-- apps
    |-- callbacks.py
    |-- config.py
    |-- layout.py
    |-- run.py
|-- assets
    |-- css
        |-- main_page.css
|-- data
|-- db_managment
    |-- data_manager.py
|-- utils
    |-- logger.py
    |-- mailing.py
    |-- utils.py
- .env
- .env.example
- .gitignore
- app.log
- experiments.ipynb 
- main.py
- Makefile
- my_db.db
- notes.txt
- README.md
- requirements.in
- requirements.txt


1) Create venv: (PS:) python -m venv venv
2) Activate venv: (PS:) source venv/Scripts/activate
3) Install packages: 
    - Use Makefile, or
    - (BASH:)
        - pip install pip-tools
        - pip-compile requirements.in 
        - pip install -r requirements.txt
4) Run main.py
5) Main.py triggers Runner which creates a demo table in our database and prepares some data
6) Page - Intro should display this data and info about the data
