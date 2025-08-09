import minescript as m
import sys
import time
import system.lib.minescript
from minescript_plus import Client,World,Gui

#spwn = World.get_spawn_pos()
print (f"spawn pos:  {World.get_spawn_pos()}")
a = World.get_day_time()#//24000
#a/=24000
print (f"daytime: {a}")

while True:
    if(World.is_thundering()):
        Gui.set_title("THUNDERSTORM")
        print("THUNDERSTORM, FREE CHARGED CREEPERS")
    if(World.is_raining()):
        Gui.set_title("RAINING")
        print("IT IS RAINING, GET YOUR RIPTIDE TRIDENT READY")
        time.sleep(10000 )
