
import requests
from bs4 import BeautifulSoup
from time import sleep
from telegram import Bot
from datatime import datatime

base = "https://www.aramex.com/track/results?mode=0&ShipmentNumber=7860913222"
catch = "Invalid number / data not currently available"

TOKEN = '590253293:AAHxmKhXGS-o-MFjELhcU_bQ3rbhVc4Hqy8'
bot = Bot(TOKEN)
id = 34015964
bot.send_message(chat_id=id, text="STARTED")

while True:


            r = requests.get(base)
            c = r.content

            soup = BeautifulSoup(c, "html.parser")


            usd = soup.find_all("div", {"class": "amx-responsive-table-faux-cell"})

            print(usd[1].text)

            if catch in usd[1].text:
                print("NOPE")
                print(datetime.now())

            else:
                bot.send_message(chat_id=id, text=base)
                exit()
                
            sleep(1800)

