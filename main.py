import win32api
import win32con
import time, datetime
import keyboard
from PIL import Image, ImageGrab
from pynput.mouse import Button, Controller

waitTime = 0.0069

def log(text):
    timestamp = datetime.datetime.utcfromtimestamp(time.time()).strftime("%H:%M:%S")
    print(f"[{timestamp}] {text}")

def click_and_move(x, y, color, mouse):
    if color == (0, 250, 0):
        tx, ty = x - 940, y - 560
        log(f"{tx}, {ty}")
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, tx, ty, 0, 0)
        time.sleep(waitTime)
        mouse.click(Button.left)
        time.sleep(waitTime)
        txx, tyx = tx * (-1), ty * (-1)
        #log(f"Restarting postion ({txx}, {tyx})")
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, txx, tyx, 0, 0)
        time.sleep(waitTime)

def main():
    print("Press Q to stop the program")
    col = [(0, 250, 0)]
    x, y = 500, 150
    mouse = Controller()
    num = 2
    image = ImageGrab.grab()
    while True:
        color = image.getpixel((x, y))
        click_and_move(x, y, color, mouse)
        
        if keyboard.is_pressed("q"):
            print("You stopped the program")
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

if __name__ == "__main__":
    main()