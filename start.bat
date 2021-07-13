python -m venv venv
CALL .\venv\Scripts\activate.bat
pip install -r requirements.txt
python OBS\manage.py makemigrations
python OBS\manage.py migrate
python OBS\manage.py runserver