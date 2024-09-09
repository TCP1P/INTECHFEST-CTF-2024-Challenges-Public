from time import sleep
from type import Status, Queue

from utils import *

import uuid
import re

MAIN_PACKAGE_NAME ="com.aimardcr.pwdmanager"
PROCESS_TIMEOUT = 5*60
CHALLENGE_NAME = "Password Manager" # Must be the same as the directory name!

FLAG = "INTECHFEST{Y4mL_Th1s_Y4Ml_Th4t_4nd_Y4mL_3v3rywh3r3}"

def callback(package_name: str, q: Queue):
    q.status = Status.RUNNING_PROOF_OF_CONCEPT

    out, _ = run_adb(['shell', 'dumpsys', 'package', MAIN_PACKAGE_NAME])
    app_uid = re.search(r"userId=(.+)", out).group(1)

    run_adb(['shell', 'mkdir', '-p', f'/data/data/{package_name}/files/'])
    run_adb(['shell', 'chmod', '777', f'/data/data/{package_name}/files/'])

    flag = "flag_" + str(uuid.uuid4()) + ".txt"
    run_adb(['shell', 'echo', FLAG, '>', f'/data/data/{MAIN_PACKAGE_NAME}/files/{flag}'])
    run_adb(['shell', 'chmod', '777', f'/data/data/{MAIN_PACKAGE_NAME}/files/{flag}'])

    run_adb(['push', f'challenges/{CHALLENGE_NAME}/pwds.yml', f'/data/data/{MAIN_PACKAGE_NAME}/files/pwds.yml'])
    run_adb(['shell', 'chmod', '777', f'/data/data/{MAIN_PACKAGE_NAME}/files/pwds.yml'])

    run_adb(['shell', 'chown', '-R', f'{app_uid}:{app_uid}', f'/data/data/{MAIN_PACKAGE_NAME}/files'])    

    start_app(package_name)

    sleep(5)

    stop_app(package_name)

    sleep(2.5)

    q.status = Status.RUNNING_VULNERABLE_APPLICATION

    sleep(0.5)

    start_app(MAIN_PACKAGE_NAME)
    sleep(2.5)

    touch_screen(70, 140)
    sleep(1.5)

    touch_screen(270, 670)
    sleep(1.5)
