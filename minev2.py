import minescript as m
import sys
import time
import lib_turn_w_direction
import test
lib_turn_w_direction.turn_w_dir("W")
direction = ["key.right","key.left"]
x = 0
m.press_key_bind("key.attack",True)
while True:
    if (m.player_get_targeted_block(4)==None):
        m.press_key_bind(direction[x%2],True)
        time.sleep(0.2)
        m.press_key_bind(direction[x%2],False)
        x+=1
    if(test.test()):
        m.press_key_bind("key.attack",True)
        print("ended")
        break
        # print("ended")

