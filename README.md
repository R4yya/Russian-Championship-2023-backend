# CyberTest backend

## The server part of the CyberTest training platform

This repository contains the backend part of the CyberTest educational platform aimed at children aged 6 to 18 years.

## Description

CyberTest is a platform designed to teach children the basics of cybersecurity using interactive tasks and exciting courses. The backend provides interaction with the database, processing requests from the front-end and content management.

## Technologies

- Django;
- Django REST framework;
- PostgreSQL;
- Swagger.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/R4yya/Russian-Championship-2023-backend.git

```

2. Move to the project directory:
```bash
cd your-path/Russian-Championship-2023-backend/cyberquest
```

3. Install dependencies:
```bash
pip install -r requirements.txt

```

4. Make and apply migrations:
```bash
python manage.py makemigrations

python manage.py migrate

```

5. Specify environment variables in .env file.

path:
```bash
your-path//Russian-Championship-2023-backend/cyberquest/.env
```

6. Create super user in order to get access to the administration panel
Use this command and foolow the instructions:
```bash
python manage.py createsuperuser
```

## Run

Start the backend server:
```bash
python manage.py runserver

```

Or specify the desired port (8000 is the default):
```bash
python manage.py runserver 0.0.0.0:8000
```

## Documentation and tools

API documentation is available on Swagger:
```bash
http://localhost:8000/swagger/
```

REST API:
```bash
http://localhost:8000/api/
```

Admin panel:
```bash
http://localhost:8000/admin/
```


## Contribution

If you want to contribute to the development of CyberTest, create a branch for new functionality or fixes, and then send a Pull Request.

## Thanks

We thank everyone who contributes to the development of this project.

## Frontend
A frontend client is also implemented for this web service using [this link.](https://github.com/Slaik1/Russian-Championship-2023)
