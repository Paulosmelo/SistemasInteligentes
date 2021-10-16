from Node import Node
from Distancias import direta, real

#f(n) função heuristica definida para descobri qual nó da fronteira utilizar

# The actual cost path from the start node to the current node. 
def g(n):
    return 0

# The actual cost path from the current node to goal node.
def h(n):
    return 0

# The actual cost path from the start node to the goal node.
def f(n):
    return  g(n) + h(n)

start = input("Start:")
line = input("Line:")
goal = input("Goal:")



start = int(start.replace("E", "")) -1
goal = int(goal.replace("E", "")) -1

initial = Node.make_node(start, 0, line)

print(initial.station)