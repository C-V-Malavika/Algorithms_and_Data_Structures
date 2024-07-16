class Graph:

    '''
    Class Graph
    Data Members
        - matrix
        - cost
        - v
        - edges
        - visited_DFS
    Member Functions
        - add_edge
        - print_graph
        - print_cost
        - DFS
        - make_set
        - sort_wrt_edges
        - kruskal
        - approx_TSP
    '''

    def __init__(self, vertices):

        '''
        Initialising values of the data members
        '''

        self.matrix = [[0 for j in range(vertices)] for i in range(vertices)]
        self.cost = [[0 for j in range(vertices)] for i in range(vertices)]
        self.v = vertices

        self.edges = {}
        self.visited_DFS = []


    def add_edge(self, start_node, end_node, cost):

        '''
        Adds an edge to the matrix representation
        and cost to the cost matrix representation
        of the graph
        '''

        self.matrix[start_node][end_node] = 1
        self.matrix[end_node][start_node] = 1

        self.cost[start_node][end_node] = cost
        self.cost[end_node][start_node] = cost

        self.edges[(start_node, end_node)] = cost


    def print_graph(self):

        '''
        Displays the matrix representation
        of the graph
        '''

        res = ""
        for item in self.matrix:
            res += str(item) + "\n"
        return res


    def print_cost(self):

        '''
        Displays the cost matrix representation
        of the graph
        '''

        res = ""
        for item in self.cost:
            res += str(item) + "\n"
        return res


    def DFS(self, start_node = 0):

        '''
        Returns the Depth First Traversal
        of the graph
        '''

        self.visited_DFS.append(start_node)

        neighbours = [i for i in range(self.v) if self.matrix[start_node][i] == 1]

        for item in neighbours:
            if item not in self.visited_DFS:
                self.DFS(item)

        return self.visited_DFS
    

    def make_set(self):

        '''
        Creating a list with vertices as sets
        '''

        lst_sets = []

        for item in g.visited_DFS:
            s = set()
            s.add(item)
            lst_sets.append(s)

        return lst_sets


    def sort_wrt_edges(self):

        '''
        Sort the edges of the graph with respect
        to cost between the edges
        '''

        return list(sorted(self.edges.items(), key = lambda item : item[1]))


    def kruskal(self):

        '''
        Implementation of kruskal's algorithm
        using greedy approach
        '''

        lst_sets = self.make_set()
        min_spanning_tree = {}
        edges = self.sort_wrt_edges()

        while len(lst_sets) != 1:

            item = edges.pop(0)
            start_node, end_node = item[0]

            Flag = False
            for s in lst_sets:
                if {start_node}.issubset(s) and {end_node}.issubset(s):
                    Flag = True

            for i in range(len(lst_sets)):
                if {start_node}.issubset(lst_sets[i]):
                    index1 = i
                if {end_node}.issubset(lst_sets[i]):
                    index2 = i

            set1, set2 = lst_sets[index1], lst_sets[index2]

            if Flag == True:
                continue
            else:
                min_spanning_tree[item[0]] = item[1]
                lst_sets.append(set1.union(set2))
                lst_sets.remove(set1)
                lst_sets.remove(set2)

        return min_spanning_tree
    

    def approx_TSP(self):

        '''
        Gives the approximate route for
        TSP problem
        '''

        min_spanning_tree = self.kruskal()
        graph = Graph(self.v)
        for item in min_spanning_tree:
            graph.add_edge(item[0], item[1], min_spanning_tree[item])

        return graph.DFS()



if __name__ == '__main__':

    g = Graph(4)

    g.add_edge(0, 1, 2)
    g.add_edge(1, 3, 9)
    g.add_edge(0, 3, 4)
    g.add_edge(2, 3, 8)
    g.add_edge(1, 2, 5)

    print("The graph matrix representation is : ")
    print("-------------------------------------")
    print(g.print_graph())

    print("The cost matrix representation is : ")
    print("------------------------------------")
    print(g.print_cost())

    print("Depth First Search : ")
    print("---------------------")
    print(g.DFS())
    print()

    print("Minimum spanning tree is")
    print("------------------------")
    print()
    print(g.kruskal())
    print()

    print("Route (After creating MST and performing DFS) : ", g.approx_TSP())
    print()

    g = Graph(7)

    g.add_edge(0, 1, 6)
    g.add_edge(0, 2, 5)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 4, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(3, 2, 2)
    g.add_edge(2, 4, 1)
    g.add_edge(4, 6, 3)
    g.add_edge(3, 5, 1)
    g.add_edge(5, 6, 3)

    print("The graph matrix representation is : ")
    print("-------------------------------------")
    print(g.print_graph())

    print("The cost matrix representation is : ")
    print("------------------------------------")
    print(g.print_cost())

    print("Depth First Search : ")
    print("---------------------")
    print(g.DFS())
    print()

    print("Minimum spanning tree is")
    print("------------------------")
    print()
    print(g.kruskal())
    print()

    print("Route (After creating MST and performing DFS) : ", g.approx_TSP())