# Jango Cam Project

## Stack:
- [TODO] React 16
- Django 2
- Python 3
- GRAPHQL

### Install dlib
Follow these guides: [here](https://www.learnopencv.com/install-dlib-on-ubuntu/)
and [here](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/)

- activate your environment, cd into dlib folder and install dlib

```bash
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --yes DLIB_USE_CUDA
```
see [pr](https://github.com/davisking/dlib/pull/1040)


1. Create virtual env.
```bash
python3.6 -m venv djangoql
source djangoql/bin/activate.fish
pip install django==2.0.3 graphene==2.0.1 graphene-django==2.0.0 django-filter==1.1.0 django-graphql-jwt==0.1.5 Pillow==5.0 Faker
pip install face_recognition
pip install -r requirements.txt
```

Particularly on macos, may need to install opencv-contrib
```bash
brew install opencv3 --with-contrib --with-python3 --without-python
```
2. Start Django
```bash
django-admin startproject jango_cam
cd jango_cam
python manage.py migrate
python manage.py runserver
```
