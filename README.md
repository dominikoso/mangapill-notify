# mangapill-notify
Simple Notification System for new Manga Chapters using telegram-chat

# How to use
1. Create bot using https://telegram.me/BotFather
2. Rename `env` to `.env`
3. Modify `MANGA_IDS` variable ex.
```
MANGA_IDS=524,5292
```
3. Linux Setup
```
$ pip3 install -r requirements.txt
$ telegram-chat --configure
$ python3 ./main.py
```
