import minescript as m
import sys
import time
import system.lib.minescript

yaw, pitch = m.player_orientation()
m.press_key_bind("key.attack",True)
if 45<=yaw<135:
    m.player_set_orientation(90,30)
elif -45>=yaw>=-135:
    m.player_set_orientation(-90,30)
elif yaw>=-135:
    m.player_set_orientation(-90,30)

elif -45<yaw<45:
    m.player_set_orientation(0,30)
else:
     m.player_set_orientation(180,30)


###NOT WORKING
