#!/usr/bin/env python3
""" Start point """

from json import dumps
from scrap_cal import start


def request():
    """ Single request """
    data = start()

    if data:
        data = list(map(
            lambda e: {'title': e[0], 'url': e[1]},
            data))

        with open('botDiscord/data.json', 'w') as result:
            result.write(dumps(data))


if __name__ == '__main__':
    request()
