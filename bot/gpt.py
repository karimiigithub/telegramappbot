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

def tikla():
    while True:
        try:
            if pyautogui.locateOnScreen('get.PNG', region=(start_x, start_y, width, height), confidence=0.4) != None:
                cords_image = pyautogui.locateOnScreen('get.PNG', confidence=0.4)
                cords_center = pyautogui.center(cords_image)
                pyautogui.click(cords_center[0]-10, cords_center[1]+10)
                print("bulundu")
                keyboard.press("f6")
                time.sleep(2.5)
                keyboard.press("f6")

            if child_window_kapat.exists():
                child_window_kapat.click()
                break

        except Exception as e:
            print("...", e)

def bug():
    while True:
        time.sleep(30)
        kapat()
        time.sleep(2)
        start()
        print("bug control")

def hata():
    while True:
        try:
            time.sleep(30)
            if pyautogui.locateOnScreen('hata.PNG', region=(start_x, start_y, width, height), confidence=0.6) != None:
                cords_hataimage = pyautogui.locateOnScreen('hata.PNG', confidence=0.6)
                cords_hatacenter = pyautogui.center(cords_hataimage)
                pyautogui.click(cords_hatacenter[0], cords_hatacenter[1])
                pyautogui.hotkey('ctrl', 'r')
                print("hata geçildi")
                time.sleep(3)
                break
        except Exception as e:
            print("hata bulunmadı", e)

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

def stop_bot():
    global bot_thread, hata_thread, bug_thread
    bot_thread.join()
    hata_thread.join()
    bug_thread.join()

# Arayüz oluşturma
root = tk.Tk()
root.title("Telegram Bot")
root.geometry("200x100")

start_button = tk.Button(root, text="Başlat", command=start_bot)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Durdur", command=stop_bot)
stop_button.pack(pady=10)

root.mainloop()


