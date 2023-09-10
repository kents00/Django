# Django 4.0.5 +
Template for Django4 + third-party programs (such as environ, argon, and django compressor).

# Folder
This is the folder where the files are stored.
```
├── src
    ├── Application
    │   ├── Templates
    │   ├── .base
    |   │   ├── base.html # This is our header and footer, all css and js are in here
    │   ├── layout
    |   │   ├── main.html # This is our front page
    |   │   ├── navbar.html # This is our navbar
    ├── Config # This is where we store our settings files
    │   ├── settings.py # This is where we store our settings
    │   ├── local.py # This is where we store our production settings
    ├── static
    │   ├── css
    │   ├── admin
    │   ├── django_extensions
    │   ├── js
    ├── manage.py
```

# Installation
- We need a virtual environment for our project to build up the environment.
```
virtualenv env
```
- Activating virtual environment
```
source env/bin/activate
```
- Installing requirements
```
pip install -r requirements.txt
```
# Deploying on Local Server
```
python manage.py runserver
```
# What are the Features?
**django-environ**
>Allows you to customize your Django application with environment variables using the Twelve-factor methodology.

**argon2-cffi**
>Is a safe password hashing algorithm. It is intended to have a tunable runtime as well as memory consumption.

**python3-memcached**
>It stores images and cuts the time it takes to load an image by more than half.

**whitenoise**
>It allows your web project to provide its own static files, making it self-contained and deployable anywhere

**django-nose**
>Testing your apps by default

**django-compressor**
>Linked and inline Javascript or CSS in a Django template is processed, combined, and minified into cacheable static assets

**django-debug-toolbar**
>Providing various debug information about the current request/response and displaying further details about the panel's content when clicked
