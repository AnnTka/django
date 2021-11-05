import logging
from time import sleep

from django_rq import job

logger = logging.getLogger(__name__)


@job
def run_products_update():
    for index in range(20):
        logger.info("run_products_update {index}")
        sleep(1)
