# Jango Cam Project

## Stack:
- [TODO] React 16
- Django 2
- Python 3
- GRAPHQL

1. Create virtual env.
```bash
python3.6 -m venv djangoql
source djangoql/bin/activate.fish
pip install django==2.0.2 graphene==2.0.1 graphene-django==2.0.0 django-filter==1.1.0 django-graphql-jwt==0.1.5
```

2. Start Django
```bash
django-admin startproject jango_cam
cd jango_cam
python manage.py migrate
python manage.py runserver
```
