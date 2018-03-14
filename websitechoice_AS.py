import pyautogui as pg
import time

pg.hotkey('winleft', 'ctrl', 'd')
pg.hotkey('winleft')
pg.typewrite('chrome\n', 0.5)

website = pg.prompt("What website do you want to visit?")

pg.typewrite((website + "\n") ,0.5)

answer = pg.confirm('Do you wan to open a new tab?')

if answer == 'OK':
    pg.hotkey('ctrl', 't')
    
