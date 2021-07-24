import requests
import telegram_send
import logging as log
import time
from datetime import datetime
from bs4 import BeautifulSoup as bs
from dotenv import dotenv_values

class Manga: 

    base_url = 'https://mangapill.com/manga/'
       
    def __init__(self, manga_id):
        self.last_chapter = 0
        self.mid = manga_id
    
    def checkManga(self):
        page = requests.get(self.base_url + self.mid)
        soup = bs(page.content, 'html.parser')
        html = list(soup.children)[3]
        chapter = html.find('a', class_='border border-color-border-primary p-1 hover:bg-color-bg-secondary')
        chapter_name = chapter.text
        chapter_link = 'https://mangapill.com' + chapter['href']

        if (self.last_chapter == 0) or (self.last_chapter != chapter_name):
            self.last_chapter = chapter_name
            message = '[!] New Chapter is available: \n- {} \n- {}'.format(chapter_name, chapter_link)
            telegram_send.send(messages=[message])
        else:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            log.info('[{}] No new chapter found for Manga {}'.format(dt_string, self.mid))

log.basicConfig(level=log.INFO)
config = dotenv_values('.env')

manga_list = []

for manga_id in config['MANGA_IDS'].split(','):
    manga_list.append(Manga(manga_id))

while True:
    for manga in manga_list:
        manga.checkManga()
        time.sleep(15)
        
    time.sleep(3600)