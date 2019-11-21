import subprocess
import tkinter


def channel_1():
    lbl.configure(text="Playing Christmas")
    lbl.pack()
    process = subprocess.Popen(['mplayer', 'http://178.32.62.163:8469'], stderr=subprocess.PIPE)


def channel_2():
    lbl.configure(text="Playing Retro Hindi")
    lbl.pack()
    process = subprocess.Popen(['mplayer', 'http://192.240.102.133:11454'], stderr=subprocess.PIPE)

if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('130x200')
    lbl = tkinter.Label(window, text="Internet Radio")
    lbl.pack()
    window.title("Radio")
    button1 = tkinter.Button(text="Christmas", fg="white", bg="blue", command=channel_1).pack()
    button2 = tkinter.Button(text="Retro Hindi", fg="white", bg="blue", command=channel_2).pack()
    window.mainloop()
