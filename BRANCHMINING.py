####NOT READY
import minescript as m
import sys
import time
from minescript_plus import Client,Gui
import ready4mining
import centre_player_lib


#put player in the centre
# CENTRE_PLAYER.center_player() #has autism - not reccomended to run
#NOW START THE LOOP

while True:
    #check player pos   
    px = m.player_position()[0] #p stands for previous
    pz = m.player_position()[2]
    pz, px = int(pz), int(px)

    #set  to pitch 25 and forward+attack                 #   straight mining
    ready4mining.ready()
    m.press_key_bind("key.forward",True)
    m.press_key_bind("key.attack",True)



                                    #         




    #when travelled 4 blocks{                            #      
    while abs(int(m.player_position()[0]) - px) < 4 and abs(int(m.player_position()[2]) - pz) < 4:
        # print("not yet")
        time.sleep(2)

    # while True:
    # print("DONE")
    m.press_key_bind("key.forward",False)
    m.press_key_bind("key.attack",False)

    #set pitch to 0 and change yaw by 90 degrees                        #
    yaw,pitch = m.player_orientation()
    yaw, pitch = int(yaw), int(pitch)
    m.player_set_orientation((yaw+90),0)

    #mine 5 blocks                                                      #
    m.press_key_bind("key.attack",True)
    time.sleep(1.2)
    m.press_key_bind("key.attack",False)
    #change yaw by 180 degrees                                          # MAKE BRANCHES
    yaw,pitch = m.player_orientation()
    yaw, pitch = int(yaw), int(pitch)
    m.player_set_orientation((yaw-180),0)

    #mine 5 blocks                                                      #
    m.press_key_bind("key.attack",True)
    time.sleep(1.2)
    m.press_key_bind("key.attack",False)
    #change yaw by 90 degrees}                                          #
    yaw,pitch = m.player_orientation()
    yaw, pitch = int(yaw), int(pitch)
    m.player_set_orientation((yaw+90),0)

    #REPEAT