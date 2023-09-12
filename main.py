import win32api, win32con
import time
import keyboard
from PIL import Image, ImageGrab
import pyautogui
from pynput.mouse import Button, Controller

col = [(0, 250, 0)]
x, y = 500, 150
mouse = Controller()
time.sleep(4)
num = 2
image = ImageGrab.grab()
color = image.getpixel((x, y))
while True:
    color = image.getpixel((x, y))
    if color == (0, 250, 0):
        tx, ty = x - 940, y - 560
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, tx, ty, 0, 0)
        time.sleep(0.00013)
        mouse.click(Button.left)
        time.sleep(0.00013)
        txx, tyx= tx * (-1), ty * (-1)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, txx, tyx, 0, 0)
        time.sleep(0.00013)
        image = ImageGrab.grab()
        x = 300
    if keyboard.is_pressed('q'):
        print('you stopped the program')
        break
    if x > 1200:
        num += 1
        if num % 2 == 0:
            x = 513
        elif num % 2 == 0:
            x = 556
        else:
            x = 587
        col = image.getpixel((320, 250))
        image = ImageGrab.grab()
    y += 100
    if y > 950:
        x += 30
        y = 150
