THIS IS TASK FOR Bit68 as an Ecommerce Simple App:

To run this app ypu wirk with the following instructions:

1 - install Docker 
2- run command docker-compose build
3- run command docker-compose run --rm app python manage.py makemigrations
4- run command docker-compose run --rm app python manage.py migrate
5- run command docker-compose run --rm app python manage.py createsuperuser and enter the following fields:
    (email, username, first_name, last_name, password)
6- run command docker-compose up
7- you can access the apis from the following urls:
    1- to register user: http://127.0.0.1:8000/api/v1/user/register/
    2- to make login: http://127.0.0.1:8000/api/v1/auth/login/
    3- to add product or get products: http://127.0.0.1:8000/api/v1/product/ must authenticated