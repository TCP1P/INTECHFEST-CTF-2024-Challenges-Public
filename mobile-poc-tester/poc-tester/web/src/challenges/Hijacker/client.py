from random import randint, uniform
from time import sleep
from type import Status, Queue

from utils import *

MAIN_PACKAGE_NAME ="com.aimar.id.hijacker"
PROCESS_TIMEOUT = 5*60
CHALLENGE_NAME = "Hijacker" # Must be the same as the directory name!

def callback(package_name: str, q: Queue):
    q.status = Status.RUNNING_PROOF_OF_CONCEPT

    grant_all_permission(package_name)

    start_app(package_name)

    sleep(2.5)

    q.status = Status.RUNNING_VULNERABLE_APPLICATION

    start_app(MAIN_PACKAGE_NAME)

    sleep(2.5)

    pin = "558102"
    run_adb(['shell', 'echo', pin, '>', f'/data/data/{MAIN_PACKAGE_NAME}/files/pin.txt'])
    run_adb(['shell', 'chmod', '777', f'/data/data/{MAIN_PACKAGE_NAME}/files/pin.txt'])

    pin_buttons = [
        {'x': 269, 'y': 1482},
        {'x': 269, 'y': 711},
        {'x': 539, 'y': 711},
        {'x': 809, 'y': 711},
        {'x': 269, 'y': 968},
        {'x': 539, 'y': 968},
        {'x': 809, 'y': 968},
        {'x': 269, 'y': 1225},
        {'x': 539, 'y': 1225},
        {'x': 809, 'y': 1225},
    ]
    clear_button = {'x': 809, 'y': 148}

    pos = 0
    while pos < len(pin):
        if randint(0, 100) < 15:
            idx = randint(0, 9)
            while idx == int(pin[pos]):
                idx = randint(0, 9)

            touch_screen(pin_buttons[idx]['x'], pin_buttons[idx]['y'])
            sleep(uniform(0.1, 0.5))

            touch_screen(clear_button['x'], clear_button['y'])
            pos = 0
        else:
            touch_screen(pin_buttons[int(pin[pos])]['x'], pin_buttons[int(pin[pos])]['y'])
            pos += 1

        sleep(uniform(0.1, 0.5))
        pass
