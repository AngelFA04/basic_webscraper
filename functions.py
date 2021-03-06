import requests
import lxml.html as html
import os
import datetime

#XPATH Expresions
HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE = '//h2[@class="headline"]/a/@href'
XPATH_TITLE = '//h1[@class="headline"]/a/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="articleWrapper  "]/p[not(@class)]/text()'
ROOT = 'Notices/'


def parse_notice(link, date):
    """ Function that parses the notice """
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"','')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)


                with open(f'{ROOT}{date}/{title}', 'w', encoding='utf-8') as f:
                    f.write(title)
                    f.write('\n\n')
                    f.write(summary)
                    f.write('\n\n')

                    {f.write(f'{p}\n') for p in body}
            except IndexError:
                return
            
        else:
            raise ValueError(f"Error: {error.status_code}")
    except ValueError as ve:
        print(ve)


def parse_home():
    """ Function to extract links from home page """
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            #(links_to_notices)

            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(ROOT+today):
                os.mkdir(ROOT+today)
            print("Saving news...")
            for link in links_to_notices:
                parse_notice(link, today)

        else:
            raise ValueError(f"Error: {response.status_code}")
    except ValueError as ve:
        print(ve)
