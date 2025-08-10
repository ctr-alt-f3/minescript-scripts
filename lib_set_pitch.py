
import minescript as m
# import sys
# import time
#import system.lib.minescript
def set(pitch):
    x =m.player_orientation()[0]

    m.player_set_orientation(x,int(pitch))