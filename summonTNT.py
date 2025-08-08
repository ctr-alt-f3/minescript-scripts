import pyautogui as pag
import time
import minescript as m
import sys
from minescript_plus import Client,Gui,Keybind

while True:
    m.execute("summon minecraft:tnt ~ ~1 ~")
    time.sleep(1)