import minescript as m
import sys
import time
import system.lib.minescript
from minescript_plus import Client

while True:
    hp = player_health()
    hp = int(hp)
    if (hp < 3):
        Client.disconnect()

