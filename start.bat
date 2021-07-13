python -m venv venv>>log.txt
CALL .\venv\Scripts\activate.bat>>log.txt
python pip install -r requirements.txt>>log.txt
echo -n makemigrations migrate | xargs -n 1 -d " " python manage.py>>log.txt