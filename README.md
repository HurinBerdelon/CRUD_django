# CRUD_django
Repository to store a simple CRUD project in Django.

## Requirements
You should have python3 installed, to run this project.

It's recommended, but not necessary, to create a virtual environment.

#### On Linux
Create the VE
<code> python3 -m venv {name_of_VE} </code> 

Activate the VE
<code> source {name_of_VE}/bin/activate</code>

#### On Windows
Create the VE
<code> python -m venv {name_of_VE} </code>

Activate the VE
<code> {name_of_VE}/Scripts/Activate</code>


With the virtual Environment created, run:
<code> pip install -r requirements.txt</code>

With django installed, run the migrations to create the database:
<code> python manage.py migrate </code

Than, initiate the project with:
<code> python manage.py runserver </code>

Open it in browser on:
<a href='http://localhost:8000'> localhost:8000 </a>


P.S. no CSS was applied to this project, it will be done in the future