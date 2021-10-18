from Node import Node
from Distancias import direta, real, lines


colors = ["azul", "amarelo", "vermelho", "verde"]

start = input("Start:")
line = input("Line:")
goal = input("Goal:")

start = int(start.replace("E", "")) -1
goal = int(goal.replace("E", "")) -1

line = colors.index(line)

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
    if not node.time > 0:
        for edge in real[currentNode.station]:
            if(edge[0] == node.station):
                time = edge[1]/30*60
                break
    else:
        time = node.time


    if not change:
        time += 4

    return currentNode.time + time

# The actual cost path from the current node to goal node.
def h(node):
    return direta[node.station][goal]

# The actual cost path from the start node to the goal node.
def f(node):
    return  g(node) + h(node)

def getLine(current, newNode):
    for i in range(len(lines)):
        if lines[i][current]  and lines[i][newNode]:
            return i;
    return 0

def getAdjecents(node): 
    adjacentsNode = []
    adjacents = real[node.station]
    for no in adjacents:
        if(not no[0] in visited):
            newNode = Node.make_node(no[0], 0, getLine(node.station, no[0]))
            newNode.time = g(newNode)
            adjacentsNode.insert(0,newNode)
        ## ver linha depois
    return adjacentsNode

def insertNode(node):
    if len(border) == 0:
        border.append((node, currentNode))
    else: 
        for i in range(len(border)):
            # if(node.station+1 == 13):
            #     print(str(node.station+1) + " - " + str(border[i][0].station+1))
            #     print(str(h(node)) + " - " + str(g(node)))
            #     print(str(h(border[i][0])) + " - " + str(g(border[i][0])))
                
            if (f(node) <= f(border[i][0])):
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
        print(str(no[0].station+1) , end=" ")
    print("")

n = goal
custo = 0

realPath = []

for node in path:
    if node[0].station == n:
        if node[0].station == goal:
            custo = node[0].time
        realPath.insert(0, node[0])
        n = node[1].station

realPath.pop(0)
print("path:", end=" ")

for node in realPath:
    print(colors[node.line], end=" => ")
    print(str(node.station+1), end=" ")
    

print("\ncusto: "+str(custo))
