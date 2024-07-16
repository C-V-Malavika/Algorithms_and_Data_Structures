class Graph:

    '''
    Class Graph
    Data Members :
        - matrix
        - v
        - vertices
        - cost
        - edges
    Member Functions
        - add_edge
        - print_cost
        - print_graph
        - make_set
        - sort_wrt_edges
        - minimum_spaning_tree
    '''

    def __init__(self, vertices):

        '''
        Initialises the values of the data members
        '''

        self.matrix = [[0 for i in range(vertices)]for j in range(vertices)]
        self.v = vertices
        self.vertices = set()
        self.cost = [[0 for i in range(vertices)]for j in range(vertices)]
        self.edges = {}


    def add_edge(self, start_node, end_node, cost):

        '''
        Adds the edge for the matrix representation
        of the graph
        '''

        self.matrix[start_node][end_node] = 1
        self.matrix[end_node][start_node] = 1

        self.cost[start_node][end_node] = cost
        self.cost[end_node][start_node] = cost

        self.edges[(start_node, end_node)] = cost

        self.vertices.add(start_node)
        self.vertices.add(end_node)


    def print_cost(self):

        '''
        Used to print the cost matrix of the graph
        '''

        string = ''
        for item in self.cost:
            string += str(item) + '\n'

        return string


    def print_graph(self):

        '''
        Used to print the matrix representation of the graph
        '''

        string = ''
        for item in self.matrix:
            string += str(item) + '\n'

        return string


    def make_set(self):

        '''
        Creating a list with vertices as sets
        '''

        lst_sets = []

        for item in g.vertices:
            s = set()
            s.add(item)
            lst_sets.append(s)

        return lst_sets


    def sort_wrt_edges(self):

        '''
        Sort the edges of the graph with respect
        to cost between the edges
        '''

        return list(sorted(g.edges.items(), key = lambda item : item[1]))


    def minimum_spaning_tree(self):

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

        return min_spanning_tree, sum(min_spanning_tree.values())


if __name__ == '__main__':

    print("CASE - 1")
    print("--------")
    print()

    g = Graph(4)

    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 5)
    g.add_edge(0, 3, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 6)
    g.add_edge(2, 3, 3)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()
    print(g.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()
    print(g.print_cost())

    print("Edges sorted based on their cost")
    print("--------------------------------")
    print()
    print(g.sort_wrt_edges())
    print()

    print("Minimum spanning tree is")
    print("------------------------")
    print()
    print(g.minimum_spaning_tree()[0])
    print()

    print("Cost of Minimum spanning tree is")
    print("--------------------------------")
    print()
    print(g.minimum_spaning_tree()[1])
    print()

    print("CASE - 2")
    print("--------")
    print()

    g = Graph(5)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(0, 3, 1)
    g.add_edge(1, 2, 5)
    g.add_edge(2, 4, 8)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()
    print(g.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()
    print(g.print_cost())

    print("Edges sorted based on their cost")
    print("--------------------------------")
    print()
    print(g.sort_wrt_edges())
    print()

    print("Minimum spanning tree is")
    print("------------------------")
    print()
    print(g.minimum_spaning_tree()[0])
    print()

    print("Cost of Minimum spanning tree is")
    print("--------------------------------")
    print()
    print(g.minimum_spaning_tree()[1])
    print()

    print("CASE - 3")
    print("--------")
    print()

    g = Graph(9)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 8, 6)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 7)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()
    print(g.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()
    print(g.print_cost())

    print("Edges sorted based on their cost")
    print("--------------------------------")
    print()
    print(g.sort_wrt_edges())
    print()

    print("Minimum spanning tree is")
    print("------------------------")
    print()
    print(g.minimum_spaning_tree()[0])
    print()

    print("Cost of Minimum spanning tree is")
    print("--------------------------------")
    print()
    print(g.minimum_spaning_tree()[1])
    print()

    print("CASE - 4")
    print("--------")
    print()

    g = Graph(6)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 5, 2)
    g.add_edge(2, 4, 4)
    g.add_edge(3, 4, 3)
    g.add_edge(5, 4, 3)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()
    print(g.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()
    print(g.print_cost())

    print("Edges sorted based on their cost")
    print("--------------------------------")
    print()
    print(g.sort_wrt_edges())
    print()

    print("Minimum spanning tree is")
    print("------------------------")
    print()
    print(g.minimum_spaning_tree()[0])
    print()

    print("Cost of Minimum spanning tree is")
    print("--------------------------------")
    print()
    print(g.minimum_spaning_tree()[1])
    print()

    print("CASE - 5")
    print("--------")
    print()

    g = Graph(5)

    g.add_edge(0, 1, 8)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 2, 9)
    g.add_edge(1, 3, 11)
    g.add_edge(2, 3, 15)
    g.add_edge(2, 4, 10)
    g.add_edge(3, 4, 7)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()
    print(g.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()
    print(g.print_cost())

    print("Edges sorted based on their cost")
    print("--------------------------------")
    print()
    print(g.sort_wrt_edges())
    print()

    print("Minimum spanning tree is")
    print("------------------------")
    print()
    print(g.minimum_spaning_tree())
    print()

    print("Cost of Minimum spanning tree is")
    print("--------------------------------")
    print()
    print(g.minimum_spaning_tree()[1])
    print()