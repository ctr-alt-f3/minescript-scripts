import minescript as m
import pyautogui
# import sys
# import time
# import system.lib.minescript
# from minescript_plus import Client,World,Gui


while True:
    m.press_key_bind("key.swapOffhand",True)
    m.press_key_bind("key.drop",True)

    m.press_key_bind("key.swapOffhand",False)
    m.press_key_bind("key.drop",False)
    m.press_key_bind("key.swapOffhand",True)
    m.press_key_bind("key.drop",True)
