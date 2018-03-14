import pyautogui as pg
import time
pg.hotkey('winleft', 'ctrl', 'd')
pg.hotkey('win')
pg.typewrite('chrome\n', 0.5)
pg.hotkey('winleft', 'up')
pg.typewrite('puns on mugs\n',0.5)
pg.click(240, 192, 1)time.sleep(10)
pg.hotkey('ctrl', 't')
pg.typewrite('puppies\n', 0.5)
pg.click(328, 231, 1)

        
