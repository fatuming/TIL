from urllib.request import urlopen 
from bs4 import BeautifulSoup
from datetime import datetime
import time
import telegram
import requests

#camera_url = 'https://smartstore.naver.com/weus/products/747069620'
mask_url = 'https://smartstore.naver.com/sangkong/products/4762917002'

bot = telegram.Bot(token='1027794161:AAFx7CM61-2aF7UcK84OdBk2POE7n6opKyY')
chat_id = -1001298145554

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
        bot.sendMessage(chat_id=chat_id, text='**상공양행**right now!!!!')
        print ("*****right now: 상공양행*****", timestamp)
        
    time.sleep(5)

        
