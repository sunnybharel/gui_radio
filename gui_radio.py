import subprocess
import tkinter
from functools import partial

# List of channels
STATION_LIST = {'Christmas': 'http://178.32.62.163:8469',
                'Old Hindi': 'http://192.240.102.133:11454',
                'Salsa': 'http://206.190.130.180:8053',
                'Classical': 'http://uk3.internet-radio.com:8060',
                'Classic Rock': 'http://95.217.68.35:8124',
                'BBC 1': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p',
                'BBC 2': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio2_mf_p',
                'BBC 3': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio3_mf_p',
                'BBC 4': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4fm_mf_p',
                'BBC 4 Ex': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4extra_mf_p',
                'BBC 6': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_6music_mf_p',
                'BBC World S': 'http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-einws',
                'BBC Scotland': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_scotlandfm_mf_p'
                }

#Set some easy variables for color
FG_COL = 'white'
BG_COL = 'blue'
BG_HLT_COL = 'white'


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

    # wraps around mplayer and starts streaming audio
    def tune(self):
        lbl.configure(text=self.text)
        lbl.pack()
        #Let's not play more than a stream at a time
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen(['mplayer', self.url], stderr=subprocess.PIPE)

if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('130x400')
    window.configure(background=BG_HLT_COL)
    lbl = tkinter.Label(window, text="Internet Radio")
    lbl.pack()
    window.title("Radio")
    radio = Radio()
    #Populate tkinter menu with buttons from station list
    for key in STATION_LIST:
        tkinter.Button(text=key, fg=FG_COL, bg="red", command=partial(radio.assign_to_obj, key)).pack()
    window.mainloop()
