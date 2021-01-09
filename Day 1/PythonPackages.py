import pyautogui as gui
import time

time.sleep(5)

gui.hotkey('win', 'r')
gui.typewrite('chrome')
gui.press("enter")
time.sleep(1)
gui.hotkey('ctrl', 'l')
time.sleep(1)
gui.typewrite('python')
gui.press("enter")
