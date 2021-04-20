import os
import subprocess
from time import sleep
from telegram import Bot

STREAM_LINK = os.environ.get('STREAM_LINK')
TELEGRAM_CHANNEL = os.environ.get('TELEGRAM_CHANNEL')
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHECK_PERIODICITY = 60  # seconds


def channel_is_live(link):
    try:
        result = str(subprocess.check_output(['streamlink', link]))
    except Exception as e:
        print(e)

    if 'result' in locals() and "Available streams:" in result:
        return True
    else:
        return False


if __name__ == '__main__':
    state = False
    while True:
        if channel_is_live(STREAM_LINK):
            if state is False:
                tg_bot = Bot(token=TELEGRAM_TOKEN)
                tg_bot.sendMessage(chat_id=TELEGRAM_CHANNEL, text=STREAM_LINK)
                del tg_bot
            state = True
        else:
            state = False
        sleep(CHECK_PERIODICITY)
