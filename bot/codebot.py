import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
from pywinauto.application import Application
import pygetwindow as gw
import multiprocessing
from pynput.mouse import Controller, Button
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

window_title = "TelegramDesktop"
windows = gw.getWindowsWithTitle(window_title)
if not windows:
    logging.error(f"No window with title '{window_title}' found.")
    exit(1)

window = windows[0]
start_x, start_y = window.left, window.top
width, height = window.width, window.height
center_x = start_x + (width / 2)
center_y = start_y + (height / 2)

try:
    app = Application(backend='uia').connect(title='TelegramDesktop')
    telegram_window = app.window(title="TelegramDesktop")
    child_window_kapat = telegram_window.child_window(title="Share", control_type="Button")
    child_window_start = telegram_window.child_window(title="battleIcon MÜCADELE battleIcon", control_type="Button")
except Exception as e:
    logging.error(f"Error connecting to TelegramDesktop application: {e}")
    exit(1)

def kapat():
    while True:
        try:
            time.sleep(5)
            logging.info('Attempting to locate newgame.PNG on the screen.')
            cords_imageshare = pyautogui.locateOnScreen('newgame.PNG', region=(start_x, start_y, width, height), confidence=0.5)
            if cords_imageshare is not None:
                cords_centershare = pyautogui.center(cords_imageshare)
                time.sleep(1)
                pyautogui.click(cords_centershare[0] + 10, cords_centershare[1] - 15)
                time.sleep(1)
            else:
                logging.info('newgame.PNG not found on the screen.')
        except pyautogui.ImageNotFoundException:
            logging.error('newgame.PNG image not found.')
        except Exception as e:
            logging.error(f"Error in kapat: {e}", exc_info=True)

def start():
    try:
        if child_window_start.exists():
            child_window_start.click()
    except Exception as e:
        logging.error(f"Error in start: {e}", exc_info=True)

def autoclicker(duration):
    mouse = Controller()
    start_time = time.time()
    while time.time() - start_time < duration:
        mouse.click(Button.left)
        time.sleep(0.09)

def tikla():
    while True:
        try:
            logging.info('Attempting to locate get.PNG on the screen.')
            cords_image = pyautogui.locateOnScreen('get.PNG', grayscale=False, region=(start_x, start_y, width, height), confidence=0.3)
            if cords_image is not None:
                cords_center = pyautogui.center(cords_image)
                pyautogui.moveTo(cords_center[0], cords_center[1])
                autoclicker(2.9)
                pyautogui.click(center_x[0]-50, center_y[1])
            else:
                logging.info('get.PNG not found on the screen.')
        except pyautogui.ImageNotFoundException:
            logging.error('get.PNG image not found.')
        except Exception as e:
            logging.error(f"Error in tikla: {e}", exc_info=True)

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

    try:
        for process in processes:
            process.start()

        for process in processes:
            process.join()
    except KeyboardInterrupt:
        for process in processes:
            process.terminate()
        logging.info("Bot stopped.")

def start_bot_with_ui():
    root = tk.Tk()
    root.title("Telegram Bot")
    root.geometry("200x100")

    start_button = tk.Button(root, text="Başlat", command=start_bot)
    start_button.pack(pady=5)

    root.mainloop()


