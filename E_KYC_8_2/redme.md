#E-kyc

#How to run

1. run redis container

```
sudo docker pull redis

sudo docker run --name some-redis -d -p  6379:6379 redis

```
2. run celery_tasks

```
celery -A celery_tasks worker --loglevel=ERROR

```
3. run main API

```

fastapi dev app.py

```