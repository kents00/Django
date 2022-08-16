
To understand this layout and how it works, please read the following:

Folder
This is the folder where the files are stored.
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

Installation 
To setup the enviroment we need a virtual enviroment for our project. 