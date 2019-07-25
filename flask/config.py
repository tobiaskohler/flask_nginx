import os

class Config(object):
    #MariaDB-URI for SQLALchemy
     #'mysql://user123:password123@db02/webapp'
    base = 'mysql://'
    user = "user123"
    password = "password123"
    host = "db02"
    database = ""
   
    SQLALCHEMY_DATABASE_URI = base + user + ':' + password + '@' + host + '/' + database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #Celery
    rabbitmq_broker_url = 'amqp://'
    rabbitmq_result_backend = 'rpc://'
    rabbitmq_user = 'user123'
    rabbitmq_password = 'password123'
    rabbitmq_host = 'rabbitmq'
    rabbitmq_venv = 'webapp'
    # 'amqp://user123:password123@localhost:5672/webapp'
    CELERY_BROKER_URL = rabbitmq_broker_url + rabbitmq_user + ':' + rabbitmq_password + '@' + rabbitmq_host + '/' + rabbitmq_venv
    # 'rpc://user123:password123@localhost:5672/webapp'
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

    #FLask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecret'