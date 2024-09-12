import pyautogui
import time
from pywinauto.application import Application
import pygetwindow as gw
import threading
from pynput.mouse import Controller, Button
import tkinter as tk



window_title = "TelegramDesktop"
window = gw.getWindowsWithTitle(window_title)[0]
start_x, start_y = window.left, window.top
width, height = window.width, window.height
center_x = start_x + (width / 2)
center_y = start_y + (height / 2)

app = Application(backend='uia').connect(title='TelegramDesktop')
telegram_window = app.window(title="TelegramDesktop")
child_window_kapat = telegram_window.child_window(title="Share", control_type="Button")
child_window_start = telegram_window.child_window(title="Düşmanı bul", control_type="Button")

def kapat():
    while True:
        try:
            time.sleep(5)
            if pyautogui.locateOnScreen('share.PNG', region=(start_x, start_y, width, height),confidence=0.5) is not None:
                cords_imageshare = pyautogui.locateOnScreen('share.PNG', confidence=0.5)
                cords_centershare = pyautogui.center(cords_imageshare)
                time.sleep(1)
                pyautogui.click(cords_centershare[0] + width // 3, cords_centershare[1])
                time.sleep(1)
                start()

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
        time.sleep(0.1)

def tikla():
    while True:
        try:
            if pyautogui.locateOnScreen('get.PNG', region=(start_x, start_y, width, height), confidence=0.3) is not None:
                cords_image = pyautogui.locateOnScreen('get.PNG', confidence=0.3)
                cords_center = pyautogui.center(cords_image)
                pyautogui.moveTo(cords_center[0], cords_center[1])
                ##autoclicker(2.9)
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
    global bot_thread, restart_thread, bug_thread
    bot_thread = threading.Thread(target=bot)
    restart_thread = threading.Thread(target=restart)
    bug_thread = threading.Thread(target=bug)

    bot_thread.start()
    restart_thread.start()
    bug_thread.start()
    update_output("Started")

# Arayüz oluşturma
root = tk.Tk()
root.title("Telegram Bot")
root.geometry("200x250")

start_button = tk.Button(root, text="Başlat", command=start_bot)
start_button.pack(pady=5)

output_label = tk.Label(root, text="", wraplength=200)
output_label.pack(pady=5)

def update_output(text):
    current_text = output_label.cget("text")
    new_text = current_text + "\n" + text
    output_label.config(text=new_text.strip())

root.mainloop()
