import minescript as m
import sys
import time
# from minescript_plus import Client,Gui
import getblocks


#why don't u use baritone???

# def tunnel_goto():
#     get player pos 
        #get_player_pos  

#     check how much in x direction 
        #target_x - current_x = goto_x (may be negative)

#     check how much in z direction 
        #target_z - current_z = goto_z (may be negative)

#     check possible exits
        #step 1: (idk how to call this)
            #if goto_x<0:
                #x_value = =1
            #else:
                #x_value = 1
            #if goto_z<0:
                #z_value = =1
            #else:
                #z_value = 1
        #final_step:
            #if getblock(x+x_value,y,z) == "minecraft:air" && getblock(x+x_value,y+1,z) == "minecraft:air":
                #x is good 
                #set isXnext to 0
            #if getblock(x,y,z+z_value) == "minecraft:air" && getblock(x,y+1,z+z_value) == "minecraft:air":
                #z is good
                #set isXnext to 1
            #else:
                #just brain hemorrhage - exit and throw an error

#       choose a "good" exit (probably just first detected) and go there

        #basic collision detection && sprint-jumping
            #set pitch to 0
            #player_press_forward(True)
            #press_key_bind(key.sprint,True)
            #while (player_get_targeted_block(1)==None)
                #press_key_bind(key.jump,True)
                #press_key_bind(key.jump,False)
            #player_press_forward(False)
            #press_key_bind(key.jump,False)
#        check if there is a way  

        #if(isXnext):
            
             #if getblock(x+x_value,y,z) == "minecraft:air" && getblock(x+x_value,y+1,z) == "minecraft:air":
                #next is good
         #else:      
             #if getblock(x,y,z+z_value) == "minecraft:air" && getblock(x,y+1,z+z_value) == "minecraft:air":
                #next is good
        ##if next is not good: just brain hemorrhage - throw an error on face or sth

        #basic collision detection && sprint-jumping
           #set pitch to 0
           #player_press_forward(True)
           #press_key_bind(key.sprint,True)
           #while (player_get_targeted_block(1)==None)
                #press_key_bind(key.jump,True)
                #press_key_bind(key.jump,False)
            #player_press_forward(False)
            #press_key_bind(key.jump,False)
        #if current_xyz == target_xyz you can be proud
        #else: just brain hemorrhage - throw an error on face or sth




