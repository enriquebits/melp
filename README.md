# melp
Django app that provide useful information about restaurants to users

## Load dummy data 

`python manage.py load_data ./restaurantes.csv`

## Available CRUD endpoints

`/restaurants/` GET/POST

`/restaurants/<id>` GET/PUT/DELETE

## Statistics endpoint 

`/restaurants/statistics?latitude=<latitude>&longitude=<longitude>&radius=<radius>` GET

It receives latitude and a longitude as parameters, which correspond to the center of a circle, and a third parameter that corresponds to a radius in METERS. 

This endpoint returns a JSON with the following data:

`{ count: Count of restaurants that fall inside the circle with center [x,y] y radius z,
   avg: Average rating of restaurant inside the circle,
   std: Standard deviation of rating of restaurants inside the circle
}`


## Installation

Using python 3.7.9

`pip install -r requirements.txt`

## Run app

Configure database in `settings.py`, then run the following command: 

`python manage.py migrate`

`python manage.py runserver`


