import minescript as m
import sys
import time
import system.lib.minescript
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



# m.player_look_at(x+1,y+yP,z)
# time.sleep(0.1)

# m.player_look_at(x,y+yP,z-1)
# time.sleep(0.1)

# m.player_look_at(x,y+yP,z+1)
# time.sleep(0.2)

# m.player_press_use(False)

# m.player_look_at(x,y-1,z)


# time.sleep(2)
m.player_press_use(False)