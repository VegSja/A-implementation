from enum import Enum
class State(Enum):
    OPEN = 1
    CLOSE = 2

def distance(startPos, endPos):
    #Using Manhattan distance 
    return abs(startPos[0]-endPos[0]) + abs(startPos[1]-endPos[1])

class AStarNode():

    def __init__(self, parent=None, position=None, map_obj=None):
        self.position = position
        self.map_obj = map_obj
        self.parent = parent
        self.calculateG(parent)
        self.calculateH(map_obj.get_goal_pos())
        self.f = self.h + self.g
        self.kids = []

    def __lt__(self, other):
        return self.f < other.f

    def calcuateF(self):
        self.f = self.h + self.g

    def calculateH(self, goal):
        self.h = distance(self.position, goal) 

    def calculateG(self, parent):
        accumulated = 0
        if parent != None:
            accumulated = parent.g
        self.g = self.map_obj.get_cell_value(self.position) + accumulated

    def generateKids(self, map_obj):
        node = AStarNode(position=[self.position[0]+1, self.position[1]], map_obj=map_obj)
        if(self.map_obj.get_cell_value(node.position) != -1):
            self.kids.append(node)

        node = AStarNode(position=[self.position[0]-1, self.position[1]], map_obj=map_obj)
        if(self.map_obj.get_cell_value(node.position) != -1):
            self.kids.append(node)

        node = AStarNode(position=[self.position[0], self.position[1]+1], map_obj=map_obj)
        if(self.map_obj.get_cell_value(node.position) != -1):
            self.kids.append(node)

        node = AStarNode(position=[self.position[0], self.position[1]-1], map_obj=map_obj)
        if(self.map_obj.get_cell_value(node.position) != -1):
            self.kids.append(node)


def propegate_path_improvements(node):
    for child in node.kids:
        attach_and_eval(child, node)
        propegate_path_improvements(child)

def attach_and_eval(child, parent, goal):
    child.parent = parent
    child.calculateG(parent)
    child.calculateH(goal)
    child.calcuateF()

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
    evaluated = []

    # Generate initial node
    firstNode = AStarNode(position=start, map_obj=map_obj)
    firstNode.g = 0
    
    # Push firstnode to openset
    openSet.append(firstNode)

    # Agenda loop
    while (len(openSet) > 0):
        inspectedNode = openSet.pop(0)
        closedSet.append(inspectedNode)

        if (inspectedNode.position == goal):
            # A* was successfull
            print("A* finished!")
            return retrace_path(inspectedNode)
            

        inspectedNode.generateKids(map_obj)
        for child in inspectedNode.kids:
            # TODO: Handle if child has previously been created
            if not isInSet(child, openSet) and not isInSet(child, closedSet):
                attach_and_eval(child, inspectedNode, goal)
                openSet.append(child)
                evaluated.append(child)
                openSet.sort()

            elif inspectedNode.g + distance(inspectedNode.position, child.position) < child.g: #Found a cheaper path to child
                attach_and_eval(child, inspectedNode, goal)
                if child in closedSet:
                    propegate_path_improvements(child)
    print("Failed!")
    return []
