import random
import pyautogui
import time
import PIL
import webcolors
import datetime

e = datetime.datetime.now()
updown = [[1128, 507], [1103, 536], [1129, 561], [1156, 535]]
i = 0
xj, yj = updown[i]
distime = 20


def get_colour_name(rgb_triplet):
    min_colours = {}
    for key, name in webcolors.CSS21_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


starttime = e.minute, e.hour, e.day
x = 1173
while 1:
    e = datetime.datetime.now()
    if e.minute >= starttime[0] + 15 or e.hour >= starttime[1] + 1 or e.day >= starttime[2] + 1:
        starttime = e.minute, e.hour, e.day
        i += 1
        if i == 4:
            i = 0
        xj, yj = updown[i]
        time.sleep(1)
        pyautogui.click(750, 313, button="left")
        time.sleep(1)
        pyautogui.click(989, 284, button="left")
        time.sleep(1.5)
        pyautogui.click(910, 335, button="left")

    time.sleep(3)
    im = PIL.ImageGrab.grab()
    imload = im.load()
    if imload[966, 485] == (251, 120, 92):
        pyautogui.click(960, 682, button="left")
    elif imload[959, 916] >= (33, 135, 153) and imload[959, 916] <= (34, 136, 153):
        time.sleep(1)
        pyautogui.click(959, 916, button="left")
    elif get_colour_name(imload[784, 893]) == "purple":
        # razz berry
        # pyautogui.click(784, 893, button="left")
        # time.sleep(2)
        # pyautogui.click(970, 879, button="left")
        # time.sleep(1)
        # pyautogui.click(970, 880, button="left")
        # time.sleep(1)
        # pyautogui.click(970, 880, button="left")
        # time.sleep(2)

        # #catch
        # pyautogui.click(970, 420, button="left")
        # pyautogui.click(970, 420, button="left")

        pyautogui.moveTo(970, 880)
        time.sleep(1)
        pyautogui.dragTo(970, 420, button='left', duration=0.12)
        time.sleep(16)
        pyautogui.click(1023, 667, button="left")
        time.sleep(2)
        pyautogui.click(956, 925, button="left")
        pyautogui.click(956, 925, button="left")

        time.sleep(2)

    time.sleep(1.5)
    pyautogui.click(xj, yj, button="left")
    pyautogui.mouseDown(button="left")
    time.sleep(distime)
    pyautogui.mouseUp(button="left")
    time.sleep(1)
    pyautogui.click(x, 122, button='left')
    pyautogui.click(x, 122, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 167, button='left')
    pyautogui.click(x, 167, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 212, button='left')
    pyautogui.click(x, 212, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 257, button='left')
    pyautogui.click(x, 257, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 302, button='left')
    pyautogui.click(x, 302, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 347, button='left')
    pyautogui.click(x, 347, button='left')
    pyautogui.dragTo(x, 122, button='left', duration=1)
    time.sleep(0.5)
    pyautogui.click(x, 122, button='left')
    pyautogui.click(x, 122, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 167, button='left')
    pyautogui.click(x, 167, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 212, button='left')
    pyautogui.click(x, 212, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 257, button='left')
    pyautogui.click(x, 257, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 302, button='left')
    pyautogui.click(x, 302, button='left')
    time.sleep(0.5)
    pyautogui.click(x, 347, button='left')
    pyautogui.click(x, 347, button='left')
    time.sleep(1)

    pyautogui.moveTo(x, 122)
    pyautogui.dragTo(x, 347, button='left', duration=1)
