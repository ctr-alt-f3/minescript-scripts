#
# get argv[1] and get all of those items from opened chest
# example:
# \s minecraft:diamond
# will steal all diamonds from opened chests

import minescript as m
import sys
import time
#import system.lib.minescript
from minescript_plus import Inventory, Screen


while True:
    try: 
        slot = Inventory.find_item(sys.argv[1],"",True)
        if slot is not None:
            list = [slot]
            Inventory.take_items(list)
            time.wait(0.2)
        # else:
        #     Screen.wait_screen()
        #     Screen.close_screen() 
           
    except:
         pass


