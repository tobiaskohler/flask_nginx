cd
export CELERY_BROKER_URL=amqp://user123:password123@rabbitmq
export CELERY_RESULT_BACKEND=rpc://user123:password123@rabbitmq
export CELERY_BROKER_HEARTBEAT=0
export CELERY_BROKER_POOL_LIMIT=None
export CELERY_BROKER_TRANSPORT_OPTIONS={'confirm_publish': True}
export CELERY_BROKER_CONNECTION_TIMEOUT=20
export CELERY_BROKER_CONNECTION_RETRY=True
export CELERY_BROKER_CONNECTION_MAX_RETRIES=100
export CELERY_TIMEZONE='UTC'
export CELERY_ENABLE_UTC=True
export CELERY_IGNORE_RESULT=False