from time import sleep
from datetime import datetime
import pyautogui
from random import randint

WIDTH = 1920 
HEIGHT = 1080
BOX_X = WIDTH - 310
BOX_Y = HEIGHT - 100
RAND_OFFSET = 100

sleep(5)
start = datetime.now().timestamp()
while True:
    rand_x = randint(RAND_OFFSET, WIDTH)
    rand_y = randint(RAND_OFFSET, HEIGHT)

    # attempt to fool twitch with random tweening
    if randint(0, 10) % 4 == 0:   # Odds = 20%
        pyautogui.moveTo(rand_x, rand_y, randint(10, 25), pyautogui.easeInQuad)
    elif randint(0, 10) % 3 == 0: # Odds = 80% * 30%
        pyautogui.moveTo(rand_x, rand_y, randint(10, 25), pyautogui.easeInBounce)
    elif randint(0, 10) % 2:      # Odds = (100% - (80% * 30%)) * 50%
        pyautogui.moveTo(rand_x, rand_y, randint(10, 25), pyautogui.easeInElastic)
    else:
        pyautogui.moveTo(rand_x, rand_y, randint(10, 25), pyautogui.easeOutQuad)

    sleep(randint(30, 90))
    end = datetime.now().timestamp()
    if(end - start > 60 * 10):
        pyautogui.moveTo(BOX_X, BOX_Y, randint(3, 12), pyautogui.easeInBounce)
        pyautogui.click()
        start = datetime.now().timestamp()
