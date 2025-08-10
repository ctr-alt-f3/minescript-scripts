import minescript as m
import sys



def is_block():
    if(m.player_get_targeted_block(sys.argv[1])):
        return 1
    else:
        return 0

