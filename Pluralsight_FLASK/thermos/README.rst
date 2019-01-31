Social bookmarking website.

Install requirements via - pip3 install -r requirements.txt

Initialize database - run commands from thermos top level directory:

python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade

Run application server:
python3 manage.py runserver