import tkinter as tk
from tkinter import messagebox
import threading
import pyautogui
import time

import pywinauto.mouse
from pywinauto.application import Application
import pygetwindow as gw
from pynput.mouse import Controller, Button

# Telegram penceresinin bilgileri
window_title = "TelegramDesktop"
window = gw.getWindowsWithTitle(window_title)[0]
start_x, start_y = window.left, window.top
width, height = window.width, window.height
center_x = start_x + (width / 2)
center_y = start_y + (height / 2)

# Telegram uygulaması
app = Application(backend='uia').connect(title='TelegramDesktop')
telegram_window = app.window(title="TelegramDesktop")
child_window_kapat = telegram_window.child_window(title="Share", control_type="Button")
child_window_start = telegram_window.child_window(title="battleIcon MÜCADELE battleIcon", control_type="Button")

# Kapatma fonksiyonu
def kapat():
    while True:
        try:
            time.sleep(5)
            if pyautogui.locateOnScreen('newgame.PNG', region=(start_x, start_y, width, height), confidence=0.5) is not None:
                cords_imageshare = pyautogui.locateOnScreen('newgame.PNG', confidence=0.5)
                cords_centershare = pyautogui.center(cords_imageshare)
                time.sleep(1)
                pyautogui.click(cords_centershare[0]+10 , cords_centershare[1]-15)
                time.sleep(1)
        except Exception as e:
            pass

def super():
    while True:
        try:
            if pyautogui.locateOnScreen('supervurus.PNG', region=(start_x, start_y, width, height), confidence=0.6) is not None:
                cords_super = pyautogui.locateOnScreen('supervurus.PNG', confidence=0.6)
                cords_centersuper = pyautogui.center(cords_super)
                time.sleep(1)
                pyautogui.click(cords_centersuper[0], cords_centersuper[1])
        except Exception as e:
            pass

# Başlatma fonksiyonu
def start():
    if child_window_start.exists():
        child_window_start.click()

# Otomatik tıklama fonksiyonu
def autoclicker(duration):
    mouse = Controller()
    start_time = time.time()
    while time.time() - start_time < duration:
        mouse.click(Button.left)
        time.sleep(0.08)

# Tiklama fonksiyonu
def tikla():
    while True:
        try:
            if pyautogui.locateOnScreen('get.PNG', grayscale=False, region=(start_x, start_y, width, height), confidence=0.3) is not None:
                cords_image = pyautogui.locateOnScreen('get.PNG', confidence=0.3, grayscale=False)
                cords_center = pyautogui.center(cords_image)
                pyautogui.moveTo(cords_center[0], cords_center[1])
                autoclicker(2.8)


        except Exception as e:
            pass

# Hata ayıklama fonksiyonu
def bug():
    while True:
        time.sleep(15)
        kapat()

# Yeniden başlatma fonksiyonu
def restart():
    while True:
        time.sleep(600)
        pyautogui.click(center_x, center_y)
        time.sleep(1)
        pyautogui.hotkey('F5')
        time.sleep(5)
        start()

# Bot işlevi
def bot():
    while True:
        start()
        time.sleep(3)
        tikla()

# Botu başlatma fonksiyonu
def start_bot():
    bot_thread = threading.Thread(target=bot)
    restart_thread = threading.Thread(target=restart)
    bug_thread = threading.Thread(target=bug)
    super_thread = threading.Thread(target=super)

    bot_thread.start()
    restart_thread.start()
    bug_thread.start()
    super_thread.start()

# Tkinter arayüzünü başlatma fonksiyonu
def start_button_clicked():
    start_bot()
    messagebox.showinfo("Başlatıldı", "Bot başarıyla başlatıldı!")

# Tkinter arayüzü
def create_gui():
    root = tk.Tk()
    root.title("PixelverseBot")
    root.geometry("100x100")

    # Başlatma düğmesi
    start_button = tk.Button(root, text="Botu Başlat", command=start_button_clicked)
    start_button.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
