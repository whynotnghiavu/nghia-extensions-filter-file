import os
import pyperclip
import pyautogui
from time import sleep


def DichTiengViet():
    text_to_copy = os.path.join(os.getcwd(), r"backup\merged.srt")
    pyperclip.copy(text_to_copy)
    
    file_tieng_viet = os.path.join(os.getcwd(), r"backup\merged.vi.srt")
    if   os.path.exists(file_tieng_viet):
        os.remove(file_tieng_viet)

    # pyautogui.hotkey('win', '1')
    # pyautogui.hotkey('win', '4')
    pyautogui.hotkey('win', '3')
    sleep(5)
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    pyautogui.typewrite(['enter'])
    # sleep(5)
    pyautogui.hotkey('ctrl', 'o')
    sleep(1)
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
    exit()
