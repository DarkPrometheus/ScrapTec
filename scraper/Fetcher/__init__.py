#!/usr/bin/env python3
""" Fetching utilities """

from os import remove, getcwd, system as cmd
from platform import system as os_type
import requests
import lxml.html as html


fake_headers = {
        'authority': 'sites.google.com',
        'method': 'GET',
        'path': '/tectijuana.edu.mx/dsc-depto-de-sistemas-y-comp/calendarios',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,\
                image/avif,image/webp,image/apng,*/*;q=0.8,application/\
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


def alternative(url):
    """ Alternative requets method """
    os_name = os_type()
    content = None

    if os_name == 'Linux':
        path = f'{getcwd()}/_scrap.html'
        cmd(f'curl {url} > {path}')
        with open(path, 'r') as html_file:
            content = html.fromstring(html_file.read())
        remove(path)

    return content


def fetch(link):
    """ Fetchs html content """
    try:
        response = requests.get(link, headers=fake_headers)
        if response.status_code == 200:
            return html.fromstring(response.content.decode('utf-8'))
        print('Error: {response.status_code}')

    except ValueError as error:
        print(error)

    return alternative(link)
