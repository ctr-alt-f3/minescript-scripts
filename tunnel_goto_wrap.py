import lib_goto
import sys
import lib_get_cords
while lib_get_cords.get()[0] != sys.argv[1] or lib_get_cords.get()[2] != sys.argv[2]:
    lib_goto.tunnel_goto(sys.argv[1],sys.argv[2])
print("ended or error")