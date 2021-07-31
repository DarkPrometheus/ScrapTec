#!/usr/bin/env python3

import requests
import lxml.html as html

fake_headers = {
        'accept': 'text/html,application/xhtml+xml,\
                application/xml;q=0.9,image/avif,image/webp,\
                image/apng,*/*;q=0.8,application/\
                signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://github.com/',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/91.0.4472.124 Safari/537.36',
        }


def fetch(link):
    """ Fetchs html content """
    try:
        response = requests.get(link, headers=fake_headers)
        if response.status_code == 200:
            return html.fromstring(response.content.decode('utf-8'))
        print('Error: {response.status_code}')

    except ValueError as err:
        print(err)

    return None
