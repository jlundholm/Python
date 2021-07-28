import pyautogui #3rd party
pyautogui.size() #screen size
width, height = pyautogui.size()
pyautogui.position() # current mouse location
pyautogui.moveTo(10, 10) #move cursor
pyautogui.moveTo(10, 10, duration=1.5) #move cursor over 1.5 secs
pyautogui.moveRel(200, 0) #move cursor relative to current location
pyautogui.click(339, 38) #click on location
pyautogui.doubleClick(339, 38)
pyautogui.rightClick(339, 38)
pyautogui.middleClick(339, 38)
pyautogui.middleClick() #clicks on current location


#to continuosly show mouse position
install pyautogui and Pillow
from terminal
py 3.9
import pyautogui
pyautogui.displayMousePosition()
