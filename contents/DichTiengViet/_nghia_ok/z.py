from modules.MyLog import MyLog


import os
import pyperclip
import pyautogui
from time import sleep


def DichTiengViet(root_dir):
    MyLog.Infor(f'root_dir: {root_dir}')

    text_to_copy = os.path.join(os.getcwd(), "backup\merged.srt")
    pyperclip.copy(text_to_copy)

    pyautogui.hotkey('win', '1')
    sleep(5)
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    sleep(5)
    pyautogui.hotkey('ctrl', 'o')
    sleep(5)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    sleep(5)
    pyautogui.hotkey('ctrl', 'shift', 'g')
    sleep(1)
    pyautogui.typewrite(['tab', 'tab', 'tab', 'tab'])
    sleep(1)
    pyautogui.typewrite(['enter'])
    sleep(5)
    exit()
    exit()
    exit()
    exit()
    exit()
