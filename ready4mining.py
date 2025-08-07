import minescript as m
import sys
import time
import system.lib.minescript
import test
from minescript_plus import Client
def ready():

    yaw, pitch = m.player_orientation()
    yaw = int (yaw)
    if -45 < yaw < 45:
        m.player_set_orientation(0, 30)
    elif 45 <= yaw < 135:
        m.player_set_orientation(90, 30)
    elif -135 < yaw < -45:
        m.player_set_orientation(-90, 30)
    else:
        m.player_set_orientation(180, 30)