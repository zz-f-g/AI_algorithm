class Node:
    def __init__(self, id: str) -> None:
        """
        This function initializes a node with an id and an empty list of successors and an empty
        dictionary of weights.
        
        :param id: the id of the node
        :type id: str
        """
        self.__id = id
        self.__successors = []
        self.__weights = {}
        # key: id of successor nodes
        # val: weight of edge

    def __repr__(self) -> str:
        return self.__id

    @property
    def id(self) -> str:
        return self.__id
    
    @property
    def successors(self) -> list:
        return self.__successors
    
    @property
    def weights(self) -> dict:
        return self.__weights
    
    def add_suc(self, node, weight: float = 1) -> None:
        """
        > The function takes a node and a weight as input and adds the node to the successors list of the
        current node
        
        :param node: the node to be added to the successors list
        :param weight: float
        :type weight: float
        """
        assert isinstance(node, Node), 'invalid node!'
        assert node not in self.__successors, 'node already exists in successors list!'
        self.__successors.append(node)
        self.__weights[node.id] = weight

class Graph:
    def __init__(self) -> None:
        self.__nodes = {}
        # key: id of nodes
        # val: node class

    @property
    def nodes(self) -> dict:
        return self.__nodes
    
    def add_node(self, id_node: str):
        """
        It adds a node to the graph
        
        :param id_node: The name of the node
        :type id_node: str
        """
        assert id_node not in self.__nodes, 'repeated node name!'
        self.__nodes[id_node] = Node(id_node)
    
    def connect_dir(self, node_src: str, node_dst: str, weight: float):
        """
        It connects two nodes in a directed graph.
        
        :param node_src: the name of the source node
        :type node_src: str
        :param node_dst: the name of the destination node
        :type node_dst: str
        :param weight: the weight of the edge
        :type weight: float
        """
        assert node_src in self.__nodes, 'source node doesn\'t exist in graph!'
        assert node_dst in self.__nodes, 'destination node doesn\'t exist in graph!'
        assert node_src != node_dst, 'same name of source and destination nodes!'
        assert weight >= 0, 'negative weight!'
        self.__nodes[node_src].add_suc(self.__nodes[node_dst], weight)

    def connect(self, node_src: str, node_dst: str, weight: float):
        """
        It adds a connection between two nodes in the graph.
        
        :param node_src: the name of the source node
        :type node_src: str
        :param node_dst: The destination node
        :type node_dst: str
        :param weight: the weight of the edge
        :type weight: float
        """
        assert node_src in self.__nodes, 'source node doesn\'t exist in graph!'
        assert node_dst in self.__nodes, 'destination node doesn\'t exist in graph!'
        assert node_src != node_dst, 'same name of source and destination nodes!'
        assert weight >= 0, 'negative weight!'
        self.__nodes[node_src].add_suc(self.__nodes[node_dst], weight)
        self.__nodes[node_dst].add_suc(self.__nodes[node_src], weight)
    
    def get_successors(self, id_node: str) -> list:
        """
        > Given a node, return a list of all the nodes that are connected to it
        
        :param id_node: the id of the node whose successors you want to get
        :type id_node: str
        :return: A list of the successors of the node with the given id.
        """
        assert id_node in self.__nodes, 'node doesn\'t exist in graph!'
        return [node.id for node in self.__nodes[id_node].successors]

    def get_weight(self, node_src: str, node_dst: str) -> float:
        """
        > The function returns the weight of the edge between the source and destination nodes
        
        :param node_src: the source node
        :type node_src: str
        :param node_dst: the destination node
        :type node_dst: str
        :return: The weight of the edge between the two nodes.
        """
        assert node_src in self.__nodes, 'source node doesn\'t exist in graph!'
        assert node_dst in self.__nodes, 'destination node doesn\'t exist in graph!'
        assert node_src != node_dst, 'same name of source and destination nodes!'
        sucs = self.__nodes[node_src].successors
        assert self.__nodes[node_dst] in sucs, 'no link between input nodes!'
        return sucs.weights[node_dst]
    
    def show(self) -> None:
        """
        It prints the id of each node, then for each successor of that node, it prints the id of the
        successor and the weight of the edge between the two nodes
        """
        for id, node in self.__nodes.items():
            print(id)
            for suc in node.successors:
                print(f'    --->{suc.id} ({node.weights[suc.id]})')
            print()

class Path:
    def __init__(self, graph: Graph, src: str) -> None:
        assert src in graph.nodes, "source node doesn\'t exist in graph!"
        self.__graph = graph
        self.__src = src
        self.__dst = src
        self.__nodes = [src]
        self.__cost = 0
    
    @property
    def dst(self) -> str:
        return self.__dst
    
    @property
    def cost(self) -> float:
        return self.__cost

    @property
    def nodes(self) -> list[str]:
        return self.__nodes

    def add_node(self, node: str) -> None:
        """
        It adds a node to the path, if the node is a successor of the end of the path.
        
        :param node: the node to add to the path
        :type node: str
        """
        assert node in self.__graph.nodes, "node does not exist in graph!"
        assert node not in self.__nodes, "node is repeated!"
        weights_dst = self.__graph.nodes[self.__dst].weights
        assert node in weights_dst, "node is not one of successors of the end of path!"
        self.__dst = node
        self.__nodes.append(node)
        self.__cost += weights_dst[node]
    
    def __str__(self) -> str:
        res = ''
        for i, node in enumerate(self.__nodes):
            if (i):
                res += '--->'
            res += node
        return res


if __name__ == '__main__':
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.connect_dir('a', 'b', 1.0)
    graph.connect_dir('b', 'c', 2.0)
    graph.connect_dir('a', 'c', 3.0)
    graph.show()
    print(graph.get_successors('a'))
    print(graph.get_successors('b'))
