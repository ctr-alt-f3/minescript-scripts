
import minescript as m
# from minescript_plus import Keybind, Gui



def get():
    x, y = m.player_orientation()
    return [(round(x,0),round(y,0))]
    # Gui.set_title("abc")



# get()