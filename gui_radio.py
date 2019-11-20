import subprocess
from easygui import *


def channel_choice():
    try:
        choice = int(input("Channel number?: "))
    except:
        print("Incorrect channel. Integers only. Try again.")
        channel_choice()


if __name__ == '__main__':
    msg = "Choose a Channel"
    choices = ["Radio 1", "BBC 3", "BBC 4", "Classic FM"]
    channel = buttonbox(msg, choices=choices)
    msgbox(channel)

    process = subprocess.Popen(['mplayer', 'http://178.32.62.163:8469'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    stdout, stderr = process.communicate()
