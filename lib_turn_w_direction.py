import minescript as m
import sys
# import time
# import math
def turn_w_dir(target_destination):
    pitch = round(m.player_orientation()[1],0)
    # pitch = round(pitch,0),
    # target_destination = sys.argv[1]
    if target_destination == "S":
        m.player_set_orientation(0,pitch)
    elif target_destination == "N":
        m.player_set_orientation(180,pitch)
    elif target_destination == "W":
        m.player_set_orientation(-90,pitch)
    elif target_destination == "E":
        m.player_set_orientation(90,pitch)
    else:
        raise Exception ("only NSWE accepted")


