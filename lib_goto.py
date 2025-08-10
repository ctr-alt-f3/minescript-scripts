import minescript as m
import sys
import time
import math
import lib_turn_w_direction
import set_pitch
# import get_cords
import lib_get_cords
import lib_set_pitch
# from minescript_plus import Client,Gui
# import get_blocks


#why don't u use baritone???

def tunnel_goto(first,second):
    isXnext = 0
    # def tunnel_goto():
    #     get player pos 
        #get_player_pos  
    x,y,z = m.player_position()
    x,y,z = math.floor(x), math.floor(y), math.floor(z)

    #     check how much in x direction 
        #target_x - current_x = goto_x (may be negative) 
    #     check how much in z direction 
    #target_z - current_z = goto_z (may be negative)
    target_x = first
    target_z = second
    goto_x = int(target_x) - x
    goto_z = int(target_z) - z


    #     check possible exits
        #step 1: (idk how to call this)
    if goto_x<0:
        x_value = -1
    else:
        x_value = 1
    if goto_z<0:
        z_value = -1
    else:
        z_value = 1
        #final_step:
    if m.getblock(x+x_value,y,z) == "minecraft:air" and m.getblock(x+x_value,y+1,z) == "minecraft:air":
                #x is good 
        # print("going X first")        
        isXnext = 0
    if m.getblock(x,y,z+z_value) == "minecraft:air" and m.getblock(x,y+1,z+z_value) == "minecraft:air":
                #z is good
        isXnext = 1
        # print("going Z first")
    #if :
    #   raise Exception("Sorry, i dont's see any exits")
                    #just brain hemorrhage - exit and throw an error

    #       choose a "good" exit (probably just first detected) and go there

    if(isXnext):
        if(z_value == 1):
            lib_turn_w_direction.turn_w_dir("S")
        else:
            lib_turn_w_direction.turn_w_dir("N")
    else:   
        if(x_value == 1):
            lib_turn_w_direction.turn_w_dir("E")
        else:
            lib_turn_w_direction.turn_w_dir("W")


        #basic collision detection && sprint-jumping
    yaw,pitch = m.player_orientation()
            #set pitch to 0
    m.player_press_forward(True)
    m.press_key_bind("key.sprint",True)
    while (m.player_get_targeted_block(1)==None ):#or lib_get_cords.get()[0] == target_x or lib_get_cords.get()[2] == target_z):
        m.press_key_bind("key.jump",True)
        # m.press_key_bind("key.jump",False)
    m.player_press_forward(False)
    m.press_key_bind("key.jump",False)
    #        check if there is a way  

    x,y,z = m.player_position()
    x,y,z = math.floor(x), math.floor(y), math.floor(z)

    if(isXnext):
            
        if m.getblock(x+x_value,y,z) == "minecraft:air" and m.getblock(x+x_value,y+1,z) == "minecraft:air":
                safe = 1
        else:      
            if m.getblock(x,y,z+z_value) == "minecraft:air" and m.getblock(x,y+1,z+z_value) == "minecraft:air":
                #next is good
                safe = 1
        #if next is not good: just brain hemorrhage - throw an error on face or sth
        if (not safe):
            raise Exception ("no safe exits")
        
    #TURNING INTO NEXT
    if(isXnext):
        if(x_value == 1):
            lib_turn_w_direction.turn_w_dir("W")
        else:
            lib_turn_w_direction.turn_w_dir("E")
    else:
        if(z_value == 1):
            lib_turn_w_direction.turn_w_dir("S")
        else:
            lib_turn_w_direction.turn_w_dir("N")
        #basic collision detection && sprint-jumping
        # yaw = m.player_orientation()[0]
            #set pitch to 0
    lib_set_pitch.set(0)
    m.player_press_forward(True)
    m.press_key_bind("key.sprint",True)
    time.sleep(1)
    # while """True:"""(m.player_get_targeted_block(1)==None):
    while (m.player_get_targeted_block(1)==None):
        m.press_key_bind("key.jump",True)
        # m.press_key_bind("key.jump",False)
    m.player_press_forward(False)
    m   .press_key_bind("key.jump",False)
    #if current_xyz == target_xyz you can be proud
        #else: just brain hemorrhage - throw an error on face or sth

        #why don't just say "ended???
    print("program ended succesfully/not succesfully")


    # tunnel_goto()