import os
from pynput import keyboard


def on_release(key):
    os._exit(0)


def exit_on_keypress():
    listener = keyboard.Listener(on_release=on_release)
    listener.start()
