from Node import Node
from Distancias import direta, real, lines


# start = input("Start:")
# line = input("Line:")
# goal = input("Goal:")

# start = int(start.replace("E", "")) -1
# goal = int(goal.replace("E", "")) -1

start = 0
goal = 9

currentNode = Node.make_node(start, 0, 0)
border = [currentNode]
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
            path.insert(0,(newNode, node))
        ## ver linha depois
    return adjacentsNode

def insertNode(node):
    if len(border) == 0:
        border.append(node)
    else: 
        for i in range(len(border)):
            if (f(node) < f(border[i])):
                border.insert(i, node)
                break
            elif ((len(border) - 1) == i):
                border.append(node)


while(len(border) > 0):
    currentNode = border.pop(0)
    visited.insert(0, currentNode.station)
    print(currentNode.station)
    if(currentNode.station == goal):
        break

    adjacents = getAdjecents(currentNode)
    # for i in adjacents:
    #     print(i.station)
    for adjacent in adjacents:
        insertNode(adjacent)
    print("border:", end=" ")
    for no in border:
        print(no.station, end=" ")
    print("")

n = goal

realPath = []

for node in path:
    if node[0].station == n:
        realPath.insert(0, node[0].station)
        n = node[1].station
    print(node[0].station)

print("path:", end=" ")
for i in realPath:
    print(i, end=" ")
