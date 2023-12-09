# CyberTest backend

## The server part of the CyberTest training platform

This repository supports the backend, a private CyberTest program aimed at children between the ages of 6 and 18.

## Description

CyberTest is a platform designed to teach children cybersecurity knowledge using interactive tools and government courses. The backend provides interaction with the database, processing requests from the front-end and content management.

## Technologies

- Django
- Django REST framework
- PostgreSQL
- Swagger

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

## Run

Start the backend server:
```bash
python manage.py runserver

```

Or specify the desired port (8000 is the default)
```bash
python manage.py runserver 0.0.0.0:8000
```

## Contribution

If you want to contribute to the development of CyberTest, create a branch for new functionality or fixes, and then send a Pull Request.

## Thanks

We thank everyone who contributes to the development of this project.

## Frontend
A frontend client is also implemented for this web service using [this link](https://github.com/Slaik1/Russian-Championship-2023)
