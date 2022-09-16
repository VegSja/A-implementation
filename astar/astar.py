from enum import Enum

def distance(startPos, endPos):
    #Using Manhattan distance 
    return abs(startPos[0]-endPos[0]) + abs(startPos[1]-endPos[1])

class AStarNode():

    def __init__(self, parent=None, position=None, goal=None, cell_value=1):
        self.position = position
        self.cell_value = cell_value
        self.parent = parent
        self.kids = []

        if(parent != None):
            self.g = parent.g + cell_value
        else:
            self.g = cell_value
        self.h = distance(position, goal)
        self.f = self.h + self.g

    def __lt__(self, other):
        return self.f < other.f


    def generateKids(self, map_obj):
        goal = map_obj.get_goal_pos()
        position=[self.position[0]+1, self.position[1]]
        node = AStarNode(position=position, parent=self, cell_value=map_obj.get_cell_value(position), goal=goal)
        if(node.cell_value != -1):
            self.kids.append(node)

        position=[self.position[0]-1, self.position[1]]
        node = AStarNode(position=position, parent=self, cell_value=map_obj.get_cell_value(position), goal=goal)
        if(node.cell_value != -1):
            self.kids.append(node)

        position=[self.position[0], self.position[1]+1]
        node = AStarNode(position=position, parent=self, cell_value=map_obj.get_cell_value(position), goal=goal)
        if(node.cell_value != -1):
            self.kids.append(node)

        position=[self.position[0], self.position[1]-1]
        node = AStarNode(position=position, parent=self, cell_value=map_obj.get_cell_value(position), goal=goal)
        if(node.cell_value != -1):
            self.kids.append(node)


def propegate_path_improvements(node):
    for child in node.kids:
        attach_and_eval(child, node)
        propegate_path_improvements(child)

def attach_and_eval(child, parent, goal):
    child.parent = parent
    child.g = parent.g + child.cell_value 
    child.h = distance(child.position, goal)
    child.f = child.h + child.g

def isInSet(node, closedSet):
    for closed in closedSet:
        if node.position == closed.position:
            return True
    return False

def retrace_path(endNode):
    path = []
    currentNode = endNode
    while True:
        if currentNode.parent == None:
            break
        currentNode = currentNode.parent
        path.append(currentNode)
    return path

def AStar(map_obj, start, goal):
    closedSet = []
    openSet = []

    # Generate initial node
    firstNode = AStarNode(position=start, goal=goal)
    
    # Push firstnode to openset
    openSet.append(firstNode)

    # Agenda loop
    while (len(openSet) > 0):
        inspectedNode = openSet.pop(0)
        closedSet.append(inspectedNode)

        if (inspectedNode.position == goal):
            # A* was successfull
            print("A* finished!")
            print(f"Inspected {len(closedSet)} nodes")
            print(f"Total cost of path: {inspectedNode.g}")
            return retrace_path(inspectedNode)
            

        inspectedNode.generateKids(map_obj)
        for child in inspectedNode.kids:
            if not isInSet(child, openSet) and not isInSet(child, closedSet):
                attach_and_eval(child, inspectedNode, goal)
                openSet.append(child)
                openSet.sort()

            elif inspectedNode.g + distance(inspectedNode.position, child.position) < child.g: #Found a cheaper path to child
                attach_and_eval(child, inspectedNode, goal)
                if child in closedSet:
                    propegate_path_improvements(child)
    print("Failed!")
    return []
