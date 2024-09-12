import pyautogui
import keyboard
import time
from pywinauto.application import Application
import pygetwindow as gw
import threading
import win32gui
import win32api
import win32con


window_title = "TelegramDesktop"
window = gw.getWindowsWithTitle(window_title)[0]
handle = window._hWnd
app = Application(backend='uia').connect(title='TelegramDesktop')
telegram_window = app.window(title="TelegramDesktop")

width, height = window.width, window.height
start_x, start_y = window.left, window.top
center_x = start_x + (width // 2)
center_y = start_y + (height // 2)
topLeft_x, topLeft_y = int((start_x + center_x)//2), int((start_y + center_y)//2)
topRight_x, topRight_y = int((start_x + center_x + width)//2), int((start_y + center_y)//2)
botLeft_x, botLeft_y = int((start_x + center_x)//2), int((start_y + center_y + height)//2)
botRight_x, botRight_y = int((start_x + center_x + width)//2), int((start_y + center_y + height)//2)

app.TelegramDesktop.print_control_identifiers()

print("Başlangıç X koordinatı:", start_x)
print("Başlangıç Y koordinatı:", start_y)
print("Genişlik:", width)
print("Yükseklik:", height)
print("TL", botLeft_x,botLeft_y)

def control_click(x, y, handle, button='left'):

    l_param = win32api.MAKELONG(x, y)

    if button == 'left':
        win32gui.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, l_param)
        win32gui.PostMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, l_param)

control_click(botLeft_x, botLeft_y, handle)




