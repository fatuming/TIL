from urllib.request import urlopen 
from bs4 import BeautifulSoup
from datetime import datetime
import time
import telegram
import requests
#should install telegrambot

#camera_url = 'url that you want'
mask_url =  'url that you want'

bot = telegram.Bot(token='token')
chat_id = id

while True:
    webpage = urlopen(mask_url)
    source = BeautifulSoup(webpage, 'html.parser')
    target = source.find('span', {'class':'buy'}).find('a')['class'][0]
    #print('********', target)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #time.sleep(10)

    if target == '_stopDefault':
#        bot.sendMessage(chat_id=chat_id, text='test: not yet')
        print ("**not yet**", timestamp)

    else:
        bot.sendMessage(chat_id=chat_id, text='****right now!!!!')
        print ("*****right now:*****", timestamp)
        
    time.sleep(5)

        
