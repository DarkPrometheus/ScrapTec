#!/usr/bin/env python3
""" Start point """

from json import dumps
from scrap_cal import start
import requests


def request(url, log=None):
    """ Single request """
    data = start()

    if data:
        if log:
            log.info('Calendario encontrado!')

        data = list(map(
            lambda e: {'title': e[0], 'url': e[1]},
            data))

        requests.post(url, data=dumps({'content': data}))
    elif log:
        log.info('Aun no esta el calendario.')


if __name__ == '__main__':
    request('http://localhost:7071/api/HttpTriggerBot')
