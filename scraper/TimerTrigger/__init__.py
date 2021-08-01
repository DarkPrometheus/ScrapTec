import logging
from main import request

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:

    if mytimer.past_due:
        logging.info('The timer is past due!')

    url = ''
    with open('bot_url.secret', 'rt') as s:
        url = str.strip(s.read())

    request(url, logging)