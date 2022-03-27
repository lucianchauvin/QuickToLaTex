import keyboard
import string
from threading import *
import sympy as sy
import pyperclip as pc
import win32clipboard
import time
from io import BytesIO
from PIL import Image


def test():
    time.sleep(.2)
    keyboard.press_and_release("ctrl + a")
    keyboard.press_and_release("ctrl + c")
    keyboard.press_and_release("backspace")
    time.sleep(.2)

    word = pc.paste()

    if word[-1] == 'l':
        word = word[:-1]

    word = '$ ' + word + " $"

    sy.preview(word, viewer='file', filename='output.png',
               dvioptions=['-D', '300'], euler=False)
    image = Image.open('output.png')
    send_to_clipboard(image)


def send_to_clipboard(image):
    output = BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


keyboard.add_hotkey('alt + l', test)

keyboard.wait()
