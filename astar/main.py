from Map import Map_Obj
from astar import *

mapobj = Map_Obj(task=2)

path = AStar(mapobj, mapobj.get_start_pos(), mapobj.get_goal_pos())
print(len(path))

mapobj.set_path_str_marker(path)
mapobj.show_map()
