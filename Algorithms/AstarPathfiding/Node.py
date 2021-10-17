#Node representado um estado por exemplo:  estação 5 linha azul e a custo em tempo atual
class Node:
    station = 0
    time = 0
    line = 0

    def __init__(self, station, time, line):
        self.station = station
        self.time = time
        self.line = line
    
    def make_node(station, time, line):
        node = Node(station, time, line)
        return node