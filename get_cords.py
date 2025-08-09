import minescript as m
import sys
import time
import system.lib.minescript
import math
from minescript_plus import Util
x, y, z = m.player_position()
x, y, z = math.floor(x), math.floor(y), math.floor(z)
string = (f"x = {x}    y = {y}   z = {z}")
Util.set_clipboard(string)
print(string)
# time.sleep(1)
m.screenshot(f"x = {x}  y = {y}   z = {z}")
