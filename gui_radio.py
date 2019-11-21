import subprocess
import tkinter
from functools import partial

STATION_LIST = {'Christmas': 'http://178.32.62.163:8469',
                'Old Hindi': 'http://192.240.102.133:11454',
                'Salsa': 'http://206.190.130.180:8053',
                'Classical': 'http://uk3.internet-radio.com:8060',
                'Classic Rock': 'http://95.217.68.35:8124',
                }
FG_COL = 'white'
BG_COL = 'blue'


class Radio:

    def __init__(self, t='', u='', p=''):
        self.text = t
        self.url = u
        self.process = p

    def assign_to_obj(self, station):
        global STATION_LIST
        self.text = station
        self.url = STATION_LIST[self.text]
        self.tune()

    def tune(self):
        lbl.configure(text=self.text)
        lbl.pack()
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen(['mplayer', self.url], stderr=subprocess.PIPE)

if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('130x200')
    lbl = tkinter.Label(window, text="Internet Radio")
    lbl.pack()
    window.title("Radio")
    radio = Radio()
    for key in STATION_LIST:
        tkinter.Button(text=key, fg=FG_COL, bg=BG_COL, command=partial(radio.assign_to_obj, key)).pack()
    window.mainloop()
