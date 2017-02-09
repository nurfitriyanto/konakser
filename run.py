import time
import pyping
import telepot

#config
## TELEGRAM_TOKEN = TELEGRAM TOKEN ID
## chat_id = TELEGRAM GROUP ID
## target = IP/Domain

#Note : processes running as root

TELEGRAM_TOKEN = '#'
CHAT_ID = '#'
TARGET = '#'

bot = telepot.Bot(TELEGRAM_TOKEN)

while True:
    req = pyping.ping(TARGET)
    if req.ret_code != 0:
        bot.sendMessage(CHAT_ID, 'Upss!! %s is offline.' % TARGET)
    
    time.sleep(30)
