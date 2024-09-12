import pyautogui
import keyboard
import time
from pywinauto.application import Application
import pygetwindow as gw
import threading
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
    if child_window_kapat.exists():
        pyautogui.click(center_x+width//3, center_y)
        clear_output()

def start():
    if child_window_start.exists():
        child_window_start.click()
        update_output("Başladı")

def autoclicker(duration):
    start_time = time.perf_counter()
    while time.perf_counter() - start_time < duration:
        pyautogui.click()
        time.sleep(0.0001)

def tikla():
    while True:
        try:
            if pyautogui.locateOnScreen('get.PNG', region=(start_x, start_y, width, height), confidence=0.3) is not None:
                cords_image = pyautogui.locateOnScreen('get.PNG', confidence=0.3)
                cords_center = pyautogui.center(cords_image)
                pyautogui.click(cords_center[0]-10, cords_center[1]+10)
                update_output("target_locked")
                autoclicker(2.8)


        except Exception as e:
            update_output(str(e))

def bug():
    while True:
        time.sleep(10)
        kapat()
        time.sleep(0.2)
        start()

def restart():
    while True:
        time.sleep(600)
        pyautogui.click(center_x, center_y)
        pyautogui.hotkey('F5')
        update_output("Refreshed")

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
    update_output("Bot başlatıldı.")

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


def clear_output():
    output_label.config(text="")
root.mainloop()
