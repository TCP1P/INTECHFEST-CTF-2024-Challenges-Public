from time import sleep
from type import Status, Queue

from utils import *

import uuid

MAIN_PACKAGE_NAME ="com.aimar.id.hidden"
PROCESS_TIMEOUT = 5*60
CHALLENGE_NAME = "Hidden" # Must be the same as the directory name!

FLAG = "INTECHFEST{remember_kids_never_hardcode_a_secret_in_your_code}"

def callback(package_name: str, q: Queue):
    q.status = Status.RUNNING_PROOF_OF_CONCEPT

    flag = "flag.txt"
    run_adb(['shell', 'echo', FLAG, '>', f'/data/data/{MAIN_PACKAGE_NAME}/files/{flag}'])
    run_adb(['shell', 'chmod', '777', f'/data/data/{MAIN_PACKAGE_NAME}/files/{flag}'])

    start_app(package_name)

    sleep(2.5)

    stop_app(package_name)

