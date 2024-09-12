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

app.TelegramDesktop.print_control_identifiers()
