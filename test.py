import minescript as m
import sys
import time
# import system.lib.minescript
from minescript_plus import Inventory, Screen 
import lib_nbt


#USED TO TEST IF PICKAXE IS NOT GONNA TO BREAK
def test():
    NETHERITE_PICKAXE = 2001
    # print(m.player_hand_items().main_hand)
    if (lib_nbt.parse_snbt(m.player_hand_items().main_hand['nbt'])['components']['minecraft:damage']>NETHERITE_PICKAXE):
        return 1
    else:
        return 0

  