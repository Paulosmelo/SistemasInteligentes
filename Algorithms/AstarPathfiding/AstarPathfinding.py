from Node import Node
from Distancias import direta, real, lines


start = input("Start:")
line = input("Line:")
goal = input("Goal:")

start = int(start.replace("E", "")) -1
goal = int(goal.replace("E", "")) -1

edge  = ()
currentNode = Node.make_node(start, 0, 0)
border = [(currentNode, currentNode)]
path = [(currentNode, currentNode)]
visited = []

#f(n) função heuristica definida para descobri qual nó da fronteira utilizar

# The actual cost path from the start node to the current node. 
def g(node):
    time = 0
    change  = lines[currentNode.line][node.station] == lines[currentNode.line][currentNode.station]

    #procurar distancia realizations
    for edge in real[currentNode.station]:
        if(edge[0] == node.station):
            time = edge[1]/30*60
            break

    if not change:
        time += 4

    return currentNode.time + time

# The actual cost path from the current node to goal node.
def h(node):
    return direta[node.station][goal]/30*60

# The actual cost path from the start node to the goal node.
def f(node):
    return  g(node) + h(node)

def getAdjecents(node): 
    adjacentsNode = []
    adjacents = real[node.station]
    for no in adjacents:
        if(not no[0] in visited):
            newNode = Node.make_node(no[0], 0, 0)
            newNode.time = g(newNode)
            adjacentsNode.insert(0,newNode)
        ## ver linha depois
    return adjacentsNode

def insertNode(node):
    if len(border) == 0:
        border.append((node, currentNode))
    else: 
        for i in range(len(border)):
            if (f(node) < f(border[i][0])):
                border.insert(i,(node, currentNode))
                break
            elif ((len(border) - 1) == i):
                border.append((node, currentNode))


while(len(border) > 0):
    edge = border.pop(0)
    currentNode = edge[0]
    visited.insert(0, currentNode.station)
    path.insert(0, edge)

    if(currentNode.station == goal):
        break

    adjacents = getAdjecents(currentNode)

    for adjacent in adjacents:
        insertNode(adjacent)
    
    print("border:", end=" ")
    for no in border:
        print(no[0].station, end=" ")
    print("")

n = goal

realPath = []

for node in path:
    if node[0].station == n:
        realPath.insert(0, node[0].station)
        n = node[1].station

print("path:", end=" ")
for i in realPath:
    print(i+1, end=" ")
