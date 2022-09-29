import graph
import copy
from collections import deque # stack
from queue import Queue # queue

class uniform_cost_search:
    def __init__(self, graph: graph.Graph, src: str, dst: str) -> None:
        assert src in graph.nodes, "source node doesn\'t exist in graph!"
        assert dst in graph.nodes, "destination node doesn\'t exist in graph!"
        assert src != dst, "same node!"
        self.__graph = graph
        self.__src = src
        self.__dst = dst

    def solve(self) -> graph.Path:
        """
        > The function takes a graph and a source and destination node, and returns the shortest path
        between them
        :return: A path from the source to the destination.
        """
        best_path = graph.Path(self.__graph, self.__src)
        paths = []
        best_index = -1
        while (True):
            if (best_index >= 0):
                if (paths):
                    best_path = paths.pop(best_index)
                else:
                    return None
            if (best_path.dst == self.__dst):
                return best_path
            sucs = self.__graph.nodes[best_path.dst].weights
            for suc in sucs:
                if (suc in best_path.nodes):
                    continue
                path = copy.deepcopy(best_path)
                path.add_node(suc)
                paths.append(path)
            min_cost = float('inf')
            for i in range(len(paths)):
                cost = paths[i].cost
                if cost < min_cost:
                    best_index = i
                    min_cost = cost

if __name__ == '__main__':
    from romania import Romania
    problem = uniform_cost_search(Romania, 'Lugoj', 'Giurgiu')
    print(problem.solve())
