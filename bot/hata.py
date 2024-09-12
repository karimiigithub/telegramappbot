import pyautogui
import keyboard
import time

while True:



    try:

        time.sleep(30)

        if pyautogui.locateOnScreen('hata.PNG', region=(1000, 100, 1800, 700), confidence=0.6) != None:
            cords_hataimage = pyautogui.locateOnScreen('hata.PNG', confidence=0.6)
            cords_hatacenter = pyautogui.center(cords_hataimage)
            pyautogui.click(cords_hatacenter[0], cords_hatacenter[1])
            pyautogui.hotkey('ctrl', 'r')
            time.sleep(3)

            if pyautogui.locateOnScreen('start.PNG', region=(1000, 100, 1800, 700), confidence=0.8) != None:
                cords_startimage = pyautogui.locateOnScreen('start.PNG', confidence=0.8)
                cords_startcenter = pyautogui.center(cords_startimage)
                pyautogui.click(cords_startcenter[0], cords_startcenter[1])
                print("5 sn içinde başlıyor")
                time.sleep(5)


    except Exception as e:
      print("hata yok:", e)