import requests
import telegram_send
import logging as log
import time
from datetime import datetime
from bs4 import BeautifulSoup as bs

URL = 'https://mangapill.com/manga/524/black-clover'
log.basicConfig(level=log.INFO)

last_chapter = 0

while True:
    page = requests.get(URL)

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    soup = bs(page.content, 'html.parser')
    html = list(soup.children)[3]
    chapter = html.find('a', class_='py-1 px-2 border border-color-border-secondary rounded text-sm')
    chapter_name = list(chapter.children)[1].text
    chapter_link = 'https://mangapill.com' + chapter['href']

    if (last_chapter == 0) or (last_chapter != chapter_name):
        last_chapter = chapter_name
        message = '[!] New Black Clover Chapter is available: \n- {} \n- {}'.format(chapter_name, chapter_link)
        telegram_send.send(messages=[message])
    else:
        log.info('[{}] No new chapter found'.format(dt_string))
        
    time.sleep(3600)