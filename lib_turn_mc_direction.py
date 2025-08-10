import minescript as m
import sys
# import time
# import math
def turn_mc_dir():
    pitch = round(m.player_orientation()[1],0)
    # pitch = round(pitch,0),
    target_destination = sys.argv[1]
    if target_destination == "+Z":
        m.player_set_orientation(0,pitch)
    elif target_destination == "-Z":
        m.player_set_orientation(180,pitch)
    elif target_destination == "-X":
        m.player_set_orientation(-90,pitch)
    elif target_destination == "+X":
        m.player_set_orientation(90,pitch)
    else:
        raise Exception ("only +X/-X/+Z/-Z accepted")
