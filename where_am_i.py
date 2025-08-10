import minescript as m
import sys
import time



x, y, z = m.player_position()
x, y, z = int(x), int(y), int(z)
m.chat(f"x = {x}    y = {y}   z = {z}")