import datetime
import logging
from main import request

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:

    if mytimer.past_due:
        logging.info('The timer is past due!')

    request()