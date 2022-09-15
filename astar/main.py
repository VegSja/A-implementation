from Map import Map_Obj
from astar import *

mapobj = Map_Obj(task=1)

path = AStar(mapobj, mapobj.get_start_pos(), mapobj.get_goal_pos())


mapobj.set_path_str_marker(path, )
mapobj.show_map()
