#!/usr/bin/env python3
""" Fetchs scholar calendar info """

from Fetcher import fetch
import lxml

SITES_URL = 'https://sites.google.com/tectijuana.edu.mx/\
        dsc-depto-de-sistemas-y-comp/calendarios'
XPATHS = {
        'links': '//section[2]//h3/div/span/a',
        }


def start():
    """ Start point """
    page_sites = fetch(SITES_URL)
    print(page_sites.xpath(XPATHS['links']))
    with open('page.html', 'w') as page:
        page.write(str(lxml.html.tostring(page_sites)))
        print('\t"page.html" saved.')


if __name__ == '__main__':
    start()
