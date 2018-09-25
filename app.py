import requests,re
from bs4 import BeautifulSoup
from time import sleep

from telegram import Bot


TOKEN = '590253293:AAHxmKhXGS-o-MFjELhcU_bQ3rbhVc4Hqy8' #this is a secret code for accessing my telegram bot
bot = Bot(TOKEN)
id = 381313636 #My telegram ID
bot.send_message(chat_id=id, text="Night Watch has Started!")

LINK = "https://ghasedak24.com/search/flight/BND-THR/1397-08-15/1-0-0"
LINK2= "https://sepehr360.com/fa/flight/b2c/oneway/showB2cFlights?origin=BND&destination=THR,IKA&departureDate=1397-08-15"

def spooky(LINK):
 try:
    r = requests.get(LINK)
    c = r.content

    soup = BeautifulSoup(c, "html.parser")

    usd = soup.find_all("span", {"class": "price"})

    list = []

    for item in usd:
        mat = re.search(r'\d{3},\d{3}', str(item))
        mat = mat.group(0)
        mat = mat.replace(",", "")
        list.append(int(mat))

    list.sort()
    return list

 except:
     pass



base = spooky(LINK)[0]   # cheapest price so far
sleep(900)

while True:
 try:

    if (spooky(LINK)[0] < base ):

        base = spooky(LINK)[0]

        mess = str(base)+" "+"Is price of Ghasedak24,But i send the Sephr360 link as well which is usually a little bit cheaper than Ghasedak"

        bot.send_message(chat_id=id, text=mess)
        bot.send_message(chat_id=id, text=str(LINK))
        bot.send_message(chat_id=id, text=str(LINK2))

    else:
        pass

    sleep(900)

 except:
     pass
