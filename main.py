import pyautogui
import time
import keyboard


if __name__ == '__main__':
    """Basic steering setup"""
    last_pressed = None
    last_pressed_time = None
    update_pressed_time = True
    while True:
        update_pressed_time = False
        if keyboard.is_pressed('t') and (last_pressed is None or time.time() - last_pressed_time > 0.3 or last_pressed != 't'):
            last_pressed = 't'
            update_pressed_time = True
            pyautogui.press('up')

        if keyboard.is_pressed('f') and (last_pressed is None or time.time() - last_pressed_time > 0.3 or last_pressed != 'f'):
            last_pressed = 'f'
            update_pressed_time = True
            pyautogui.press('left')

        if keyboard.is_pressed('g') and (last_pressed is None or time.time() - last_pressed_time > 0.3 or last_pressed != 'g'):
            last_pressed = 'g'
            update_pressed_time = True
            pyautogui.press('down')

        if keyboard.is_pressed('h') and (last_pressed is None or time.time() - last_pressed_time > 0.3 or last_pressed != 'h'):
            last_pressed = 'h'
            update_pressed_time = True
            pyautogui.press('right')

        if update_pressed_time:
            last_pressed_time = time.time()
