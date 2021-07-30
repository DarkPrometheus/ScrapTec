#!/usr/bin/env python3
import requests
import lxml.html as html
import os
import datetime

page = 'https://www.tijuana.tecnm.mx/categoria/tec-noticias/'
fake_headers = {
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/91.0.4472.124 Safari/537.36'
        }
Links = '//h2/a/@href'
Titles = "//h2[@class='entry-title']/text()"
Desc = "//article/div[@class='entry-content']/p/text()"

def parse_notice(link, today):
    try:
        response = requests.get(link, headers=fake_headers)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(Titles)[0]
                title = title.replace('\"', '').strip()

                if len(parsed.xpath(Desc)) > 2:
                    summary = ""
                    for i in parsed.xpath(Desc):
                        summary = summary + i
                else:
                    summary = parsed.xpath(Desc)[0]

            except:
                print("Error en la noticia: " + changeName(title))
                return
            
            ruta = "res/" + today + "/" + changeName(title) + ".txt"
            with open(ruta, "w", encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def changeName(title):
    i = 0
    temp = ""
    while i < 20:
        temp = temp + title[i]
        i = i + 1

    return temp


def parse_home():
    try:
        response = requests.get(page, headers=fake_headers)
        if response.status_code == 200:
            Home = response.content.decode('utf-8')
            parsed = html.fromstring(Home)
            parsedLinks = parsed.xpath(Links)

            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir("res/" + today):
                os.mkdir("res/")
                os.mkdir("res/" + today)

            print(len(parsedLinks))
            for link in parsedLinks:
                parse_notice(link, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

if __name__ == '__main__':
    parse_home()
