from bs4 import BeautifulSoup
import requests
import lxml.html as html
import os
import datetime

page = 'https://cnnespanol.cnn.com/seccion/tecnologia/'

Links = '//div[@class="module__content row--container"]/div/article/div/a/@href'
Titles = '//div[@class="col--main"]/article/div[@class="news__data"]/h1/text()'
Desc = '//div[@class="col--main"]/article/div[@class="news__data"]/div[@class="news__excerpt"]/p/text()'


def parse_notice(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(Titles)[0]
                title = title.replace('\"', '').strip()
                print("Title: ", title)
                if len(parsed.xpath(Desc)) > 2:
                    summary = ""
                    for i in parsed.xpath(Desc):
                        summary = summary + i
                else:
                    summary = parsed.xpath(Desc)[0]

            except:
                return

            open(f'{today}/{title}.txt', "x")
            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(page)
        if response.status_code == 200:
            Home = response.content.decode('utf-8')
            parsed = html.fromstring(Home)
            parsedLinks = parsed.xpath(Links)

            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)

            for link in parsedLinks:
                parse_notice(link, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()
