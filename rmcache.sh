rm -rf account/__pycache__
rm -rf account/migrations/__pycache__
rm -rf account/migrations/00*

rm -rf blog/__pycache__
rm -rf blog/migrations/__pycache__
rm -rf blog/migrations/00*

rm db.sqlite3

python manage.py migrate
python manage.py makemigrations	
python manage.py migrate

python manage.py createsuperuser
