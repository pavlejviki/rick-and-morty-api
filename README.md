### How to run:
- Create venv: 'python -m venv venv'
- Activate it: 'venv\Scripts\activate'
- Install requirements: 'pip install -r requirements.txt'
- Run migrations: 'python manage.py migrate'
- Run Redis server: 'docker run -d -p 6379:6379 redis'
- Run celery worker for tasks handling: 'celery -A rick_and_morty_api worker -l INFO -P solo'
- Run celery beat for task scheduling: 'celery -A rick_and_morty_api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler'
- Create schedule for running sync in DB
- Run app: 'python mange.py runserver'
