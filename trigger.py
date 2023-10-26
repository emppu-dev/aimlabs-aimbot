from pynput.mouse import Controller, Button
import win32api
import win32con
import time
import datetime
import keyboard
from PIL import Image, ImageGrab

def log(text):
    timestamp = datetime.datetime.utcfromtimestamp(time.time()).strftime("%H:%M:S")
    print(f"[{timestamp}] {text}")

mouse = Controller()

def click_if_green():
    screen_width, screen_height = ImageGrab.grab().size
    x, y = screen_width // 2, screen_height // 2
    image = ImageGrab.grab(bbox=(x - 1, y - 1, x + 1, y + 1))
    color = image.getpixel((1, 1))
    
    if color == (0, 250, 0):
        log(f"{x}, {y}")
        mouse.position = (x, y)
        mouse.click(Button.left)

def triggerbot():
    print("Press Q to stop the program")

    while True:
        click_if_green()

        if keyboard.is_pressed("q"):
            print("You stopped the program")
            break

if __name__ == "__main__":
    triggerbot()