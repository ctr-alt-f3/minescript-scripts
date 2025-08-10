#getblocklist(positions: List[List[int]]) -> List[str]
import minescript as m
import minescript_plus as m_plus
import time
import math


def lava_warning():
    x, y, z = m.player_position()
    print("start scanning\n\n")
    for cx in range (-2,2):
        for cy in range (-2,2):
            for cz in range (-2,2):
                print(m.getblock(x+cx,y+cy,z+cz))
                if "minecraft:lava" in (m.getblock(x+cx,y+cy,z+cz)):
                       return 1
                # print(m.getblock(x+cx,y+cy,z+cz))
                # if("minecraft:lava[level=0]" == m.getblock(x+cx,y+cy,z+cz)):
                #     print("found")


# if(lava_warning()):
#      print("found")