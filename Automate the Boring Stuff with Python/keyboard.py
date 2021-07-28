import pyautogui
pyautogui.click(100,100) #make sure program is in focus
pyautogui.typewrite('Hello World', interval=0.2)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)
pyautogui.KEYBOARD_KEYS # run in idle to list all keys
pyautogui.press('f1')
pyautogui.hotkey('ctrl', 'o')
