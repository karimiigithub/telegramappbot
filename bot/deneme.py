import pyautogui
import keyboard
import time
import pygetwindow as gw


window_title = "TelegramDesktop"


window = gw.getWindowsWithTitle(window_title)[0]


start_x, start_y = window.left, window.top


width, height = window.width, window.height

print("Başlangıç X koordinatı:", start_x)
print("Başlangıç Y koordinatı:", start_y)
print("Genişlik:", width)
print("Yükseklik:", height)

if pyautogui.locateOnScreen('start.PNG', region=(start_x, start_y, width, height), confidence=0.8) != None:
    cords_startimage = pyautogui.locateOnScreen('start.PNG', confidence=0.8)
    cords_startcenter = pyautogui.center(cords_startimage)
    pyautogui.click(cords_startcenter[0], cords_startcenter[1])
    print("5 sn içinde başlıyor")
    time.sleep(5)

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

            time.sleep(0.5)

            if pyautogui.locateOnScreen('close.PNG', region=(start_x, start_y, width, height), confidence=0.6) != None:
                cords_endimage = pyautogui.locateOnScreen('close.PNG', confidence=0.6)
                cords_endcenter = pyautogui.center(cords_endimage)
                pyautogui.click(cords_endcenter[0], cords_endcenter[1]+470)
                pyautogui.click(cords_endcenter[0], cords_endcenter[1] + 470)

                print("oyun bitti")

                if pyautogui.locateOnScreen('start.PNG', region=(start_x, start_y, width, height), confidence=0.6) != None:
                    cords_startimage = pyautogui.locateOnScreen('start.PNG', confidence=0.6)
                    cords_startcenter = pyautogui.center(cords_startimage)
                    time.sleep(1.5)
                    pyautogui.click(cords_startcenter[0], cords_startcenter[1])
                    print("bulundu")



        except Exception as e:

            print("bulunamadı:", e)