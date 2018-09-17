
import requests 
from bs4 import BeautifulSoup
from time import sleep
from telegram import Bot
from datetime import datetime
from pytz import timezone

format = "%Y-%m-%d %H:%M:%S"

base = "https://www.aramex.com/track/results?mode=0&ShipmentNumber=7860913222"

TOKEN = '590253293:AAHxmKhXGS-o-MFjELhcU_bQ3rbhVc4Hqy8'
bot = Bot(TOKEN)
id = 34015964
bot.send_message(chat_id=id, text="STARTED")

r = requests.get(base)
old_content = r.content
sleep(60)

while True:


            r = requests.get(base)
            new_content = r.content



            if old_content == new_content:
                print("no change")
                now_gmt = datetime.now(timezone("GMT"))
                now_asia = now_gmt.astimezone(timezone('Asia/Tehran'))
                print(now_asia.strftime(format))
            else:
                now_gmt = datetime.now(timezone("GMT"))
                now_asia = now_gmt.astimezone(timezone('Asia/Tehran'))
                print(now_asia.strftime(format))        
                        
                bot.send_message(chat_id=id, text=base)
                bot.send_message(chat_id=id, text=str(now_asia.strftime(format)))
                        
                print("change happend")



            old_content = new_content
            sleep(1800)
