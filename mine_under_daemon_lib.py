import minescript as m
# import minescript_plus as m_plus
#import time
import math




def air_daemon():
    x, y ,z = m.player_position()
    x, y, z = math.floor(x),math.floor(y),math.floor(z)
    if "minecraft:air" == (m.getblock(x, y-2, z)):
        print (m.getblock(x, y-2, z))

def lava_daemon():
    x, y ,z = m.player_position()
    x, y, z = math.floor(x),math.floor(y),math.floor(z)
    if "minecraft:lava" in (m.getblock(x, y-2, z)):
        print (m.getblock(x, y-2, z))
    # print(m.getblock(x, y-2, z))
