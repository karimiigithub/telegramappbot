import pyautogui
import time
from pywinauto.application import Application
import pygetwindow as gw
import multiprocessing
from pynput.mouse import Controller, Button



window_title = "TelegramDesktop"
window = gw.getWindowsWithTitle(window_title)[0]
start_x, start_y = window.left, window.top
width, height = window.width, window.height
center_x = start_x + (width / 2)
center_y = start_y + (height / 2)

app = Application(backend='uia').connect(title='TelegramDesktop')
telegram_window = app.window(title="TelegramDesktop")
child_window_kapat = telegram_window.child_window(title="Share", control_type="Button")
child_window_start = telegram_window.child_window(title="battleIcon MÜCADELE battleIcon", control_type="Button")

def kapat():
    while True:
        try:
            time.sleep(5)
            if pyautogui.locateOnScreen('newgame.PNG', region=(start_x, start_y, width, height),confidence=0.5) is not None:
                cords_imageshare = pyautogui.locateOnScreen('newgame.PNG', confidence=0.5)
                cords_centershare = pyautogui.center(cords_imageshare)
                time.sleep(1)
                pyautogui.click(cords_centershare[0]+10 , cords_centershare[1]-15)
                time.sleep(1)
                #start()

        except Exception as e:
            pass

def start():
    if child_window_start.exists():
        child_window_start.click()


def autoclicker(duration):
    mouse = Controller()
    start_time = time.time()
    while time.time() - start_time < duration:
        mouse.click(Button.left)
        time.sleep(0.08)

def tikla():
    while True:
        try:
            if pyautogui.locateOnScreen('get.PNG', grayscale=False, region=(start_x, start_y, width, height), confidence=0.3) is not None:
                cords_image = pyautogui.locateOnScreen('get.PNG', confidence=0.3, grayscale=False)
                cords_center = pyautogui.center(cords_image)
                pyautogui.moveTo(cords_center[0], cords_center[1])
                autoclicker(2.9)
        except Exception as e:
            pass

def bug():
    while True:
        time.sleep(15)
        kapat()



def restart():
    while True:
        time.sleep(600)
        pyautogui.click(center_x, center_y)
        time.sleep(1)
        pyautogui.hotkey('F5')
        time.sleep(5)
        start()

def bot():
    while True:
        start()
        time.sleep(3)
        tikla()

def start_bot():
    processes = []

    bot_process = multiprocessing.Process(target=bot)
    restart_process = multiprocessing.Process(target=restart)
    bug_process = multiprocessing.Process(target=bug)

    processes.append(bot_process)
    processes.append(restart_process)
    processes.append(bug_process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    start_bot()




