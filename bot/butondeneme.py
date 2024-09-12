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
child_window_kapat = telegram_window.child_window(title="Kapat", control_type="Button")
child_window_start = telegram_window.child_window(title="Düşmanı bul", control_type="Button")

def kapat():
    if child_window_kapat.exists():
        child_window_kapat.click()
        time.sleep(1)


def start():
    if child_window_start.exists():
        child_window_start.click()
        update_output("Searching...")
        time.sleep(3)

# Global değişkenlerin tanımlanması
running = True

# İşlevlerin tanımlanması

def update_output(message):
    print(message)  # Güncelleme çıktısı

def autoclicker(duration):
    start_time = time.perf_counter()
    while time.perf_counter() - start_time < duration and running:
        pyautogui.click()
        time.sleep(0.1)

def tikla():
    global running
    while running:
        try:
            if pyautogui.locateOnScreen('get.PNG', region=(start_x, start_y, width, height), confidence=0.3) is not None:
                cords_image = pyautogui.locateOnScreen('get.PNG', confidence=0.3)
                cords_center = pyautogui.center(cords_image)
                pyautogui.leftClick(cords_center[0]-10, cords_center[1]+10)
                update_output("target_locked")
                autoclicker(2.5)
        except Exception as e:
            update_output(str(e))
    update_output("tikla thread terminated")

def refresh():
    global running
    while running:
        time.sleep(300)
        pyautogui.click(center_x, center_y)
        pyautogui.hotkey('F5')
        update_output("Refreshed")

def bot():
    while running:
        start()
        kapat()

def start_bot():
    global bot_thread, refresh_thread, click_thread, running
    running = True
    bot_thread = threading.Thread(target=bot)
    refresh_thread = threading.Thread(target=refresh)
    click_thread = threading.Thread(target=tikla)

    bot_thread.start()
    refresh_thread.start()
    click_thread.start()
    update_output("Started")

def stop_threads():
    global running
    running = False
    bot_thread.join()
    refresh_thread.join()
    click_thread.join()
    update_output("All threads terminated")

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
