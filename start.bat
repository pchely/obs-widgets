@echo off
python -m venv venv
CALL .\venv\Scripts\activate.bat
python pip install -r requirements.txt
echo -n makemigrations migrate | xargs -n 1 -d " " python manage.py