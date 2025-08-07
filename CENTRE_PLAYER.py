import minescript as m
import minescript_plus as m_plus
import time
import math


#has authism but who cares

def release_all_movement_keys():
    for key in ["key.forward", "key.left", "key.back", "key.right", 'key.sneak']:
        m.press_key_bind(key,False)

def center_player():
    try:
        x, y, z = m.player_position()
        target_x = int(x) + 0.5
        target_z = int(z) + 0.5

        tolerance = 0.005  
        timeout = time.time() + 2

        m.press_key_bind('key.sneak',True)

        while time.time() < timeout:
            current_x, _, current_z = m.player_position()

            is_x_centered = abs(current_x - target_x) < tolerance
            is_z_centered = abs(current_z - target_z) < tolerance

            if is_x_centered and is_z_centered:
                break  

            if not is_x_centered:
                if current_x < target_x:
                    m.press_key_bind("key.right",True)
                    m.press_key_bind("key.left",False)
                else:
                    m.press_key_bind("key.left",True)
                    m.press_key_bind("key.right",False)
            else:
                m.press_key_bind("key.left",False)
                m.press_key_bind("key.right",False)

            if not is_z_centered:
                if current_z > target_z:
                    m.press_key_bind("key.forward",True)
                    m.press_key_bind("key.back",False)
                else:
                    m.press_key_bind("key.back",True)
                    m.press_key_bind("key.forward",False)
            else:
                m.press_key_bind("key.forward",False)
                m.press_key_bind("key.back",False)
            
            time.sleep(0.01)

        m.echo("Wycentrowano!")

    except Exception as e:
        m.echo(f"ERROR: {e}")
    finally:
     
        release_all_movement_keys()




