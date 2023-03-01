## Getting started

This project has been made only for study porpouses, it allows you to administrate budgets for each category of your expenses, manage your accounts and so on.

It uses docker for local usage and local development. 

### Prerequisites

You just need to have **docker** and been logged.

## Installation (for Windows)
```bash
git clone https://github.com/kardashq/finance.git
```
   `.env.example` - please rename it to `.env` and install you settings.

Then you just need to build the images and containers, this is done just once with:

```bash
docker-compose up -d
```
### Run the App

In order to run the app in each subsecuent execution just use:


  ```bash
  docker-compose start
  ```
to create a superuser use:
```bash
docker exec -it container_id python manage.py createsuperuser
```
### Stop the app

```bash
docker-compose stop
```

### Remove the containers
```bash
docker-compose down
```
**Note:** due to the volumes, the database info is persistent, to remove it permanently use:

```bash
dacker-compose down -v
```
**You can see the documentation at:**

-   `http://localhost:8000/swagger/`

## Built With

-   [Python](https://www.python.org/downloads/) 3.10
-   [Django Rest Framework](https://www.django-rest-framework.org/) 3.14
-   [Docker](https://www.docker.com/)


## Project Status

It's already working, but I'm currently working on it.
