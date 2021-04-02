import time

import pusher
from celery import shared_task
from celery.utils.log import get_task_logger
from decouple import config

logger = get_task_logger(__name__)


channels_client = pusher.Pusher(
    app_id=config('APP_ID'),
    key=config('KEY'),
    secret=config('SECRET'),
    cluster=config('CLUSTER'),
    ssl=True
)


@shared_task(queue='fila1')
def print_numbers(max_number):
    logger.info('Creating the task..')

    _sec = 3
    logger.info('Aguardar {} seg'.format(_sec))
    time.sleep(_sec)
    for i in range(max_number):
        logger.info(i)

    logger.info('Finishing task..')
    channels_client.trigger(
        'my-channel', 'my-event',
        {'message': 'Finalizada com sucesso!'}
    )
    return True
