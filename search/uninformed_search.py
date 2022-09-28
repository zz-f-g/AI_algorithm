import graph
from collections import deque
from queue import Queue

class uninformed_search:
    def __init__(self, graph: graph.Graph, src: str, dst: str) -> None:
        assert src in graph.nodes, "source node doesn\'t exist in graph!"
        assert dst in graph.nodes, "destination node doesn\'t exist in graph!"
        assert src != dst, "same node!"
        self.__graph = graph
        self.__src = src
        self.__dst = dst
    
    @property
    def graph(self) -> graph.Graph:
        return self.__graph
    
    def bfs(self) -> bool:
        explored = set()
        frontier = Queue()
        frontier.put(self.__src)
        while (frontier):
            node = frontier.get()
            if node in explored:
                continue
            explored.add(node)
            print(node)
            if node == self.__dst:
                print("Find it!")
                return True
            sucs = self.__graph.nodes[node].successors
            for suc in sucs:
                if suc.id not in explored:
                    frontier.put(suc.id)
        print("Can not find it!")
        return False
    
    def dfs(self) -> bool:
        explored = set()
        frontier = deque()
        frontier.append(self.__src)
        while (frontier):
            node = frontier.pop()
            explored.add(node)
            print(node)
            if node == self.__dst:
                print("Find it!")
                return True
            sucs = self.__graph.nodes[node].successors
            for suc in sucs:
                if suc.id not in explored:
                    frontier.append(suc.id)
        print("Can not find it!")
        return False
    
if __name__ == "__main__":
    from romania import Romania
    problem = uninformed_search(Romania, 'Lugoj', 'Eforie')
    print("Deepth First Search:")
    problem.dfs()
    print()
    print("Breadth First Search:")
    problem.bfs()
