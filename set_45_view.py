
import minescript as m
import sys
import time
#import system.lib.minescript

#when your yaw == 45 degree you travel 2% faster


yaw, pitch = m.player_orientation()
yaw, pitch = int(yaw), int (pitch)

print(f"previous yaw: {yaw}\nprevious pitch: {pitch}")

#do not change pitch

if -90>yaw>=-180:
    m.player_set_orientation(-135,pitch)
elif 0>yaw>=-90:
     m.player_set_orientation(-45,pitch)
elif 45>yaw>=0:
      m.player_set_orientation(45,pitch)
else:
      m.player_set_orientation(135,pitch)