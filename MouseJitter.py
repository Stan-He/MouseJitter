import tkinter as Tkinter
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

    def __init__(self, width=256, height=160):
        self.countdown = 120  # 初始倒计时时间
        self._alive = True
        self.thrd = None  # 初始化线程对象为None
        self._setup_gui(width, height)  # 先创建GUI
        self.start_countdown()  # 启动倒计时

    def start_countdown(self):
        """启动倒计时"""
        if not self._alive:  # 如果程序正在关闭，不继续更新
            return
            
        # 先显示当前数字
        self.countdown_label.config(text=str(self.countdown))
        
        if self.countdown > 0:
            # 减少计数
            self.countdown -= 1
            # 安排下一次更新
            if self._alive:  # 再次检查是否正在关闭
                self.root.after(1000, self.start_countdown)
        else:
            # 倒计时结束，移动鼠标并重置
            self.move_mouse(self.random_value(), self.random_value())
            self.countdown = 120
            # 立即开始新的倒计时
            if self._alive:  # 再次检查是否正在关闭
                self.start_countdown()

    def _setup_gui(self, w, h):
        self.root = Tkinter.Tk()
        self.root.title('Mouse Jitter')
        self.root.protocol(name='WM_DELETE_WINDOW', func=self.click_exit)
        
        # 创建主框架
        self.frame = Tkinter.Frame(self.root)
        
        # 创建倒计时标签
        self.countdown_label = Tkinter.Label(
            self.frame,
            text=str(self.countdown),
            font=('Arial', 72),  # 字体大小增加到原来的3倍（24 * 3 = 72）
            width=4  # 设置固定宽度，防止数字变化时窗口大小改变
        )
        self.countdown_label.pack(pady=10)
        
        # 创建退出按钮
        self.button = Tkinter.Button(self.frame, text='Exit')
        self.button.bind('<Button-1>', self.click_exit)
        self.button.pack()
        
        self.frame.pack(pady=h/2, padx=w/2)
        # 启动倒计时
        self.root.after(1000, self.start_countdown)
        self.root.mainloop()

    def click_exit(self, *args):
        self._alive = False  # 设置标志，停止所有更新
        self.root.after(100, self.root.destroy)  # 延迟销毁窗口，确保所有操作都已完成
        if self.thrd and self.thrd.is_alive():
            self.thrd.join()

    def _start_thread(self):        
        self.thrd = threading.Thread(target=self.worker)
        self.thrd.daemon = True  # 设置为守护线程
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
        self.root.after(0, self.start_countdown)  # 使用after方法启动倒计时
        while self._alive:
            time.sleep(1)

if __name__ == '__main__':
    mj = MouseJitter()
