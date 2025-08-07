import minescript as m
import sys
import time
import system.lib.minescript

#m.execute('/item replace entity @p hotbar.0 with minecraft:fishing_rod')

# map_enchants = [
#     "minecraft:luck_of_the_sea 3",
#     "minecraft:lure 3",
#     "minecraft:unbreaking 3",
#     "minecraft:mending 1"
# ]

# #for ench in map_enchants:
#    m.execute(f"/enchant @p {ench}")




def find_bobber():
    for entity in m.entities():
        if "fishing_bobber" in entity.type.lower():
            return entity
    return None

# def wait4bite(bobber, timeout=30):
#     start = time.time()
#     last_y = bobber.position[1]
#     while time.time() - start < timeout:
#         entity = find_bobber()
#         if entity:
#             y = entity.position[1]
#             if y - last_y > 0.2:
#                 return True
#             last_y = y
#         time.sleep(0.1)
#     return False

def wait4bite(bobber, timeout=30):
    start = time.time()
    last_y = bobber.position[1]
    while time.time() - start < timeout:
        entity = find_bobber()
        if entity:
            y = entity.position[1]
            if y - last_y > 0.2:
                return True
            last_y = y
        time.sleep(0.1)
    return False

# with m.EventQueue() as events:
#     events.register_chat_listener()
while True:
    m.player_press_use(True)
    m.player_press_use(False)
    time.sleep(2)
    bobber = find_bobber()
    if bobber and wait4bite(bobber):
        m.echo("ZNALEZIONO")
        m.player_press_use(True)
        m.player_press_use(False)
        # event = events.get()
        # if event.type == m.EventType.CHAT and "ide" in event.message.lower():
        #       break
      