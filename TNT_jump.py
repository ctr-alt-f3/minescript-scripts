import minescript as m
import sys
import time
import system.lib.minescript


TNTslot = 0
PPslot = 0
for item in m.player_inventory():
   # print(f"slot: {item.slot}: {item.item}x{item.count}")
    if item.item == "minecraft:tnt":
        TNTslot = item.slot
    if item.item == "minecraft:bamboo_pressure_plate":
        PPslot = item.slot


m.player_inventory_select_slot(TNTslot)

x, y, z = m.player_position()
print(f"{x},\n{y},\n{z}")


yP=0.5

# m.player_look_at(x-1,y+yP,z)




m.player_press_use(True)


X = 0 
Y = 50
m.player_set_orientation(X,Y)
time.sleep(0.2)
X+=90
m.player_set_orientation(X,Y)
time.sleep(0.2)
X+=90
m.player_set_orientation(X,Y)
time.sleep(0.2)
X+=90
Y+=10
m.player_set_orientation(X,Y)
time.sleep(0.2)
m.player_look_at(x,y-1,z)

m.player_inventory_select_slot(PPslot)
time.sleep(0.2)
m.player_press_use(False)
m.player_press_jump(True)
time.sleep(16)
m.player_press_jump(False)