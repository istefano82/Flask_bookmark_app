Cash Receipt Manager is an OCR (optical character recognition) application for storing and analyzing cash receipt documents

Setup project: 1. Clone the project and setup virtualenv 2. Install the packages in requirements.txt

To start the application navigate to toplevel crm directory and execute:

python manage.py dropdb # drop the database. Used when changes to the models are made.
python manage.py initdb # initialize the database
python manage.py runsever # Starts the webserver
Open webbrowser and navigate to: http://localhost:5000/index
