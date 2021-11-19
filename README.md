# Django 3.2.9 +

## About ##
In minutes, you can create a fully working Django website that includes several essential third-party apps.

```
src                   
├── manage.py
├── /static
├── /media
├── /config            
│   ├── settings.py    
│   ├── local.py  
│   ├── urls.py        
│   ├── .env
|   
├── /Application           
│   ├── urls.py
|   ├── views.py
|   ├── models.py
|   ├── /templates
|      ├── .base
|      ├── layout 
...
```

## Installation ##
If you're not setting up a virtual environment,[visit here](https://virtualenv.pypa.io/en/latest/installation.html#via-pip).
- Create your working environment and virtualenv:
```
$ virtualenv environment
```
- activating virtualenv:
```    
$ source environment/bin/activate
$ cd src
```
- installing requirements:
```    
$ pip install -r requirements.txt
```

## Features ##
This project template comes with the following features by default:

Templates:
- django_compressor for javascript/css/less/sass compression
- whitenoise own static files will be served

Security:
- argon2-cffi for password hashing default configuration
- django-environ-2 for securing your credentials

Caching:
- python-memcached

Admin:
- for development and production, django-debug-toolbar is included

Testing:
- django-nose
