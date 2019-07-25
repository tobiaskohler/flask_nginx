import os
from celery import Celery
import time

#Celery
rabbitmq_broker_url = 'amqp://'
rabbitmq_result_backend = 'rpc://'
rabbitmq_user = 'user123'
rabbitmq_password = 'password123'
rabbitmq_host = 'rabbitmq'          #####IMPORTANT!! NAME OF THE DOCKER-COMPOSE INTERNAL SERVICE!!!!
rabbitmq_venv = ''
# 'amqp://user123:password123@rabbitmq:5672/webapp'
CELERY_BROKER_URL = rabbitmq_broker_url + rabbitmq_user + ':' + rabbitmq_password + '@' + rabbitmq_host + '/' + rabbitmq_venv
# 'rpc://user123:password123@rabbitmq:5672/webapp'
CELERY_RESULT_BACKEND = rabbitmq_result_backend + rabbitmq_user + ':' + rabbitmq_password + '@' + rabbitmq_host + '/' + rabbitmq_venv
CELERY_BROKER_HEARTBEAT = 0
CELERY_BROKER_POOL_LIMIT = None
CELERY_BROKER_TRANSPORT_OPTIONS = {'confirm_publish': True}
CELERY_BROKER_CONNECTION_TIMEOUT = 20
CELERY_BROKER_CONNECTION_RETRY = True
CELERY_BROKER_CONNECTION_MAX_RETRIES = 100
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True
CELERY_IGNORE_RESULT = False

# CELERY_BROKER_URL=amqp://user123:password123@rabbitmq
# CELERY_RESULT_BACKEND=rpc://user123:password123@rabbitmq
# CELERY_BROKER_HEARTBEAT=0
# CELERY_BROKER_POOL_LIMIT=None
# CELERY_BROKER_TRANSPORT_OPTIONS={'confirm_publish': True}
# CELERY_BROKER_CONNECTION_TIMEOUT=20
# CELERY_BROKER_CONNECTION_RETRY=True
# CELERY_BROKER_CONNECTION_MAX_RETRIES=100
# CELERY_TIMEZONE='UTC'
# CELERY_ENABLE_UTC=True
# CELERY_IGNORE_RESULT=False

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND, enable_utc=CELERY_ENABLE_UTC, timezone=CELERY_TIMEZONE,
                            task_ignore_result=CELERY_IGNORE_RESULT, BROKER_POOL_LIMIT=CELERY_BROKER_POOL_LIMIT,
                            broker_connection_timeout=CELERY_BROKER_CONNECTION_TIMEOUT, broker_connection_retry=CELERY_BROKER_CONNECTION_RETRY,
                            broker_connection_max_retries=CELERY_BROKER_CONNECTION_MAX_RETRIES)


@celery.task(name='testtask')
def Testtask(n):
    n = int(n[0])

    for i in range(n):
        print(i)
        print(f"noch {n-1} Zufallszahlen zu erledigen!")
        time.sleep(5)

    return f"Finish, Gesamtdauer: {n}"