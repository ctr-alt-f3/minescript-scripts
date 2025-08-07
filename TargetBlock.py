import minescript as m

# Face forward
# m.player_set_orientation(0, 0)

# Get the targeted block
block = m.player_get_targeted_block(10)
if block:
    m.echo(f"Target Block: {block.type} @ {block.position} {block.nbt}")
else:
    m.echo("No block in crosshairs")