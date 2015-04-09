import Tkinter
import threading
import time
import random
import sys
import ctypes
from functools import partial

class MouseJitter(object):
    MOUSEEVENTF_MOVE = 0x0001 # mouse move
    MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down
    MOUSEEVENTF_LEFTUP = 0x0004 # left button up
    MOUSEEVENTF_RIGHTDOWN = 0x0008 # right button down
    MOUSEEVENTF_RIGHTUP = 0x0010 # right button up
    MOUSEEVENTF_MIDDLEDOWN = 0x0020 # middle button down
    MOUSEEVENTF_MIDDLEUP = 0x0040 # middle button up
    MOUSEEVENTF_WHEEL = 0x0800 # wheel button rolled
    MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move
    SM_CXSCREEN = 0
    SM_CYSCREEN = 1

    def __init__(self, width=1024, height=640):
        self._start_thread()
        self._setup_gui(width, height)

    def _setup_gui(self, w, h):
        self.root = Tkinter.Tk()
        self.root.title('Mouse Jitter')
        self.root.protocol(name='WM_DELETE_WINDOW', func=self.click_exit)
        self.frame = Tkinter.Frame(self.root)
        self.button = Tkinter.Button(self.frame, text='Exit')
        self.button.bind('<Button-1>', self.click_exit)
        self.button.pack()
        self.frame.pack(pady=h/2, padx=w/2)
        self.root.mainloop()

    def click_exit(self, *args):
        self._alive = False
        self.thrd.join()
        self.root.destroy()
        self.root.quit()

    def _start_thread(self):        
        self._alive = True
        self.thrd = threading.Thread(target=self.worker)
        self.thrd.start()

    def __repr__(self):
        return 'MouseJitter()'
    __str__ = __repr__

    def move_mouse(self, x_delta, y_delta):
        ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_MOVE, x_delta, y_delta, 0, 0)

    def random_value(self, limit=10):
        v = int(limit * random.random())
        return v if int(2 * random.random()) < 1 else -v

    def worker(self):
        while self._alive:
            self.move_mouse(self.random_value(), self.random_value())
            time.sleep(1)

if __name__ == '__main__':
    mj = MouseJitter()
