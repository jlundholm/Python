import pyautogui

pyautogui.screenshot('c:\\screenshot_example.png')
pyautogui.locateOnScreen('c:\\calc7key.png') # returns location of something from an image
pyautogui.locateCenterOnScreen('c:\\calc7key.png')
pyautogui.moveTo((932,336),duration=1)
pyatuogui.click(932, 336)

