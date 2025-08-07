import minescript as m
import sys
import time
import system.lib.minescript

# m.chat("abc")
# m.player_press_forward(True)
# m.player_press_jump(True)
# time.sleep(5)
# m.player_press_forward(False)
# m.player_press_jump(False)
# m.player_set_orientation(0,0)
# for a in range (360):
#     m.player_set_orientation(a,0)
# a = 0

a = 0
nr_of_spins = int(sys.argv[1]) * 360
speed = int(sys.argv[2])
while(a<nr_of_spins):
    a+=speed

    m.player_set_orientation(a,0)
