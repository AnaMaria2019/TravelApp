# TravelApp


## Getting Started

Follow all the steps below if you want to get this project up and running on your computer.

### Prerequisites

* [Pycharm Community](https://www.jetbrains.com/pycharm/) - version 2020.1
* [Python](https://www.python.org/downloads/release/python-360/) - version 3.6
* Django Framework - version 2.2.8

### Setup steps

* Create a <strong>Pycharm</strong> project:
  * <strong>Step 1</strong>: Create project
  * <strong>Step 2</strong>: Complete the 'Location' field with the location where you want to create the project
  * <strong>Step 3</strong>: Select in the 'Project Interpreter:New Virtualenv environment' field the 'New environment using Virtualenv'
  * <strong>Step 4</strong>: Add the path, from your computer, to the Python interpreter in the 'Base interpreter' field
  * <strong>Step 5</strong>: Click 'Create'

* Install <strong>Django</strong> in your project's venv:
  * <strong>Step 1</strong>: Make sure that the Python interpreter is your local venv. To check this go to 'File' -> 'Settings' -> 'Project: <name_of_the_project>'-> 'Python Interpreter' and here select your venv if it's not selected already.
  * <strong>Step 2</strong>: Make sure that when you open 'Terminal' from Pycharm you have the venv activated (if you don't type the following command: `venv\Scripts\avtivate` and press Enter). If the venv is activated it will appear like this '(venv)' in the front of the line (Example: '(venv) D:\1_Ana\3_Info\11_Facultate\Anul_III\Licenta\TravelApp\travelapp>')
  * <strong>Step 3</strong>: Open <strong>Terminal</strong> and run the following command: `pip install Django==2.2.8`
  
* Create a Django project within the Pycharm project just created:
  * In 'Terminal' type `django-admin startproject <project_name>`
  * In 'Terminal' type `cd <project_name>` to enter in the project's directory
  * In 'Terminal' type `python manage.py startapp <app_name>` to create a Django app
