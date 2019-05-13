# movie_importer

Nozbe recruitment task

## Prerequisites

To start you have to have installed `Python 3.7.2`

## Getting Started
To start the project locally

Clone repository
```
$ git clone https://github.com/szymon6927/movie_importer.git
```

I recommend using  `virtualenv`
```
$ virtualenv venv

for unix users:
$ source venv/bin/activate 

for windows users:
$ source venv/Scripts/activate
```

then 
```
$ cd movie_importer
```

next step is to install all required packages
```
$ pip install -r requirements.txt
```

before running app, make all needed migrations
```
$ python manage.py migrate
```

now you can start
```
$ python manage.py runserver
```

open a browser and go to
```
http://127.0.0.1:8000
```

## Import data

To import data run
```
$ python manage.py import --names path_to_name.tsv --titles path_to_title.tsv
```

These command will run script which imports data into DB

## Requirements

I decided to use a few third-party libraries. Here is the reasoning behind choosing them

- Django REST framework - powerful toolkit for building APIs, the huge community, great eco-system, a lot of education materials
- Django REST Swagger - for me Swagger UI is the best UI toolkit for automatically generated API documentation
- pandas - the best high-performance tool for data analysis

## Authors

* **Szymon Miks** - [website](https://szymonmiks.pl/)

