import minescript as m
import sys
import time
import system.lib.minescript

block = m.player_get_targeted_block(10)
if(block):
    m.echo(f"{block.type}   {block.position}")
else:

    m.echo("no block found")

