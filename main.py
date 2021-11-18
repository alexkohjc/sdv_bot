import numpy as np
import pyautogui
import time

def main():
    
    # initialize pyautogui
    pyautogui.FAILSAFE = True

    # countdown timer
    print('Starting', end='')
    
    for i in range(3):
        print('.', end='')
        time.sleep(1)
    print('go')

    # do anything
    pyautogui.keyDown('w')
    time.sleep(0.5)
    pyautogui.keyUp('w')
    pyautogui.keyDown('s')
    time.sleep(0.5)
    pyautogui.keyUp('s')

    print('Done')

if __name__ == "__main__":
    main()
