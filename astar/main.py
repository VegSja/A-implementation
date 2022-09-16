from Map import Map_Obj
from astar import *

mapobj = Map_Obj(task=4)

path = AStar(mapobj, mapobj.get_start_pos(), mapobj.get_goal_pos())

mapobj.set_path_str_marker(path)

# Write start and goal positon after path
mapobj.set_goal_pos_str_marker()
mapobj.set_start_pos_str_marker()

mapobj.show_map()
