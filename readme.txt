All python commands:

pip install django
django-admin startproject python_website
cd python_website
python manage.py startapp myapp
python manage.py migrate
python manage.py runserver
python manage.py makemigration myapp
python manage.py sqlmigrate myapp 001
python manage.py migrate myapp
python manage.py createsuperuser