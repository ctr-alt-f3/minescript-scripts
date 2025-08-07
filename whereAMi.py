import minescript as m
import sys
import time



x, y, z = m.player_position()
x, y, z = int(x), int(y), int(z)
print(f"x = {x}    y = {y}   z = {z}")