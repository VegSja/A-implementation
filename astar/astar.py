from enum import Enum
class State(Enum):
    OPEN = 1
    CLOSE = 2

class AStarNode():

    def __init__(self, parent=None, position=None, status=State.OPEN):
        self.position = position
        self.g = 0
        self.h = 0
        self.f = self.h + self.g
        self.status = status
        self.parent = parent
        self.kids = []

    def calcuateF(self):
        self.f = self.h + self.g

    # TODO: Should be changed
    def calculateH(self, goal):
        self.h = self.g

    # TODO: Should be changed
    def generateKids(self):
        return []

def distance(startPos, endPos):
    #Using Manhattan distance 
    return abs(startPos.x-endPos.x) + abs(startPos.y-endPos.y)

def propegate_path_improvements(node):
    for child in node.kids:
        attach_and_eval(child, node)
        propegate_path_improvements(child)

def attach_and_eval(child, parent):
    child.parent = parent
    child.g = parent.p + distance(child, parent)
    child.calculateH()
    child.calcuateF()


def AStar(mapMatrix, start, goal):
    closedSet = []
    openSet = []
    
    # Generate initial node
    firstNode = AStarNode(position=start)
    firstNode.g = 0
    firstNode.calculateH(goal)
    firstNode.calcuateF()
    
    # Push firstnode to openset
    openSet.append(firstNode)

    # Agenda loop
    while (len(openSet) > 0):
        inspectedNode = openSet.pop(0)
        closedSet.append(inspectedNode)

        if (inspectedNode == goal):
            # A* was successfull
            print("A* finished!")
            break

        inspectedNode.generateKids()
        for child in inspectedNode.kids:
            # TODO: Handle if child has previously been created
            if child not in openSet and child not in closedSet:
                attach_and_eval(child, inspectedNode)
                openSet.append(child)

            elif inspectedNode.g + distance(inspectedNode, child) < child.g: #Found a cheaper path to child
                attach_and_eval(child, inspectedNode)
                if child in closedSet:
                    propegate_path_improvements(child)
                
            






