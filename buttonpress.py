from pyautogui import *
from pynput import keyboard

def on_press(key):
    global x
    x = 0
    if int(x) == 1 :
        click()
    try:
        print(x)
        if key.char == 'p':
            click()
            x = 1
            
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
     key))
    if key == keyboard.Key.esc:
        # Stop listener
        x = 0
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
