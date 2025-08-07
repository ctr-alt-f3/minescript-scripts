import minescript as m
import sys
import time
import system.lib.minescript


x, y, z = m.player_position()
x, y, z = int(x), int(y), int(z)
print(f"x = {x}    y = {y}   z = {z}")
# time.sleep(1)
m.screenshot(f"x = {x}  y = {y}   z = {z}")
