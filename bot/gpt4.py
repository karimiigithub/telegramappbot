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

app = Application(backend='uia').connect(title='TelegramDesktop')
telegram_window = app.window(title="TelegramDesktop")
child_window_kapat = telegram_window.child_window(title="Kapat", control_type="Button")
child_window_start = telegram_window.child_window(title="Düşmanı bul", control_type="Button")

def kapat():
    if child_window_kapat.exists():
        child_window_kapat.click()

def start():
    if child_window_start.exists():
        child_window_start.click()

def autoclicker(duration):
    start_time = time.perf_counter()
    while time.perf_counter() - start_time < duration:
        pyautogui.click()
        time.sleep(0.0001)

def tikla():
    while True:
        try:
            if pyautogui.locateOnScreen('get.PNG', region=(start_x, start_y, width, height), confidence=0.4) is not None:
                cords_image = pyautogui.locateOnScreen('get.PNG', confidence=0.4)
                cords_center = pyautogui.center(cords_image)
                pyautogui.click(cords_center[0]-10, cords_center[1]+10,duration=0)
                update_output("target_locked")
                autoclicker(2.5)

            if child_window_kapat.exists():
                child_window_kapat.click()
                break

        except Exception as e:
            update_output(str(e))

def bug():
    while True:
        time.sleep(30)
        kapat()
        time.sleep(2)
        start()
        update_output("Bug kontrol ediliyor...")

def hata():
    while True:
        try:
            time.sleep(15)
            if pyautogui.locateOnScreen('hata.PNG', region=(start_x, start_y, width, height), confidence=0.6) is not None:
                cords_hataimage = pyautogui.locateOnScreen('hata.PNG', confidence=0.6)
                cords_hatacenter = pyautogui.center(cords_hataimage)
                pyautogui.click(cords_hatacenter[0], cords_hatacenter[1])
                pyautogui.hotkey('ctrl', 'r')
                update_output("Hata geçildi")
                time.sleep(3)
                break
        except Exception as e:
            update_output("Hata bulunmadı " + str(e))

def bot():
    while True:
        start()
        time.sleep(3)
        tikla()
        kapat()

def start_bot():
    global bot_thread, hata_thread, bug_thread
    bot_thread = threading.Thread(target=bot)
    hata_thread = threading.Thread(target=hata)
    bug_thread = threading.Thread(target=bug)
    bot_thread.start()
    hata_thread.start()
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

root.mainloop()
