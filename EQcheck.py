import minescript as m
import sys
import time
import system.lib.minescript

for item in m.player_inventory():
    print(f"slot: {item.slot}: {item.item}x{item.count}\n NBT: {item.nbt}\n\n")



for item in m.player_inventory():
    print(f"slot: {item.slot}: {item.item}x{item.count}")

# hands = m.player_hand_items()
# m.echo(f"prawa reka: {hands.main_hand.items}")
# m.echo(f"lewa reka: {hands.off_hand.items}")

