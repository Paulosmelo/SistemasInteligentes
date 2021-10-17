from Node import Node
from Distancias import direta, real, lines

#f(n) função heuristica definida para descobri qual nó da fronteira utilizar

# The actual cost path from the start node to the current node. 
def g(node):
    return 

# The actual cost path from the current node to goal node.
def h(node):
    return 0

# The actual cost path from the start node to the goal node.
def f(node):
    return  g(node) + h(node)

def getAdjecents(node): 
    adjacentsNode = []
    adjacents = real[node.station]
    for no in adjacents:
        adjacentsNode.insert(Node.make_node(no[0], f(no), 0))
        ## ver linha depois
    return adjacentsNode

def insertNode(border, node):
    if len(border) == 0:
        border.append(node)
    else: 
        for i, n in enumerate(border):
            if (node.time < n.time):
                border.insert(i, node)
                break
            elif ((len(border) - 1) == i):
                border.append(node)

start = input("Start:")
line = input("Line:")
goal = input("Goal:")

start = int(start.replace("E", "")) -1
goal = int(goal.replace("E", "")) -1

border = [Node.make_node(start, 0, line)]
path = []

while(len(border) > 0):
    currentNode = border.pop(0)
    if (currentNode.station == goal):
        print('result')
        # como printar rotaa??
    else:
        adjacents = getAdjecents(currentNode)
        for adjacent in adjacents:
            insertNode(border, adjacent)