# -*- coding:utf -8 -*- 
#!/usr/bin/env python3 

import os 
import logging 
import datetime 
from time import sleep
from telethon import TelegramClient 

os.system('cls||clear') 
 
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.CRITICAL)


# Input your own API hash & id values  
api_id = 2234296
api_hash = '7fb298fb96d173643085f22bd9ecf79b'
client = TelegramClient('anon', api_id, api_hash)
# Client connect
client.start() 

print('\t|~~~>SPAMTEG - Telegram Spamer<~~~|\n')
# Your message for spam 
message = input('Input message text:~~>')
# Input *.txt file full of usernames
import_file = input('Input file:~~> ') # Chats/users for spam
# Time
timers = datetime.datetime.today() 
sleep_time = 7
# Spam function
async def spam(): 
    all_participants = open(import_file, 'r')  
    for participant in all_participants: 
        if participant is  not None:
            try:
                # Send message for chats
                await client.send_message(participant, message)  
                print('I send message:', participant, '\ttime: ', timers.strftime('%H.%M.%S'))
                sleep(sleep_time)
                print('Waiting {} seconds...'.format(sleep_time))
            except PeerFloodError:
                print(colored('Getting Flood Error from telegram. Script is stopping now. Please try again after some time.', 'red'))
                client.disconnect()
            except Exception as e:
                print('Error:', e)
                print('Trying to continue...')
with client:
 client.loop.run_until_complete(spam())