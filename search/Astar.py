from graph import *

if __name__ == '__main__':
    romania = Graph()
    romania.add_node('Arad')
    romania.add_node('Bucharest')
    romania.add_node('Craiova')
    romania.add_node('Drobeta')
    romania.add_node('Eforie')
    romania.add_node('Fagaras')
    romania.add_node('Giurgiu')
    romania.add_node('Hirsova')
    romania.add_node('Iasi')
    romania.add_node('Lugoj')
    romania.add_node('Mehadia')
    romania.add_node('Neamt')
    romania.add_node('Oradea')
    romania.add_node('Pitesti')
    romania.add_node('Rimnicu Vilcea')
    romania.add_node('Sibiu')
    romania.add_node('Timisoara')
    romania.add_node('Urziceni')
    romania.add_node('Vaslui')
    romania.add_node('Zerind')
    romania.connect('Oradea', 'Zerind', 71)
    romania.connect('Oradea', 'Sibiu', 151)
    romania.connect('Arad', 'Zerind', 75)
    romania.connect('Arad', 'Sibiu', 140)
    romania.connect('Arad', 'Timisoara', 118)
    romania.connect('Lugoj', 'Timisoara', 111)
    romania.connect('Lugoj', 'Mehadia', 70)
    romania.connect('Drobeta', 'Mehadia', 75)
    romania.connect('Drobeta', 'Craiova', 120)
    romania.connect('Rimnicu Vilcea', 'Craiova', 146)
    romania.connect('Pitesti', 'Craiova', 138)
    romania.connect('Rimnicu Vilcea', 'Pitesti', 97)
    romania.connect('Rimnicu Vilcea', 'Sibiu', 80)
    romania.connect('Fagaras', 'Sibiu', 99)
    romania.connect('Fagaras', 'Bucharest', 211)
    romania.connect('Pitesti', 'Bucharest', 101)
    romania.connect('Giurgiu', 'Bucharest', 90)
    romania.connect('Urziceni', 'Bucharest', 85)
    romania.connect('Urziceni', 'Hirsova', 98)
    romania.connect('Eforie', 'Hirsova', 86)
    romania.connect('Urziceni', 'Vaslui', 142)
    romania.connect('Iasi', 'Vaslui', 92)
    romania.connect('Iasi', 'Neamt', 87)
    romania.show()