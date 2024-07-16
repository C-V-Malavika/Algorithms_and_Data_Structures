import math

class Graph:

    '''
    Class Graph
    Data Members :
        - matrix
        - cost
        - v
        - edges
    Member Functions
        - add_edge
        - print_cost
        - print_graph
        - bellman_ford
    '''

    def __init__(self, vertices):

        '''
        Initialises the values of the data members
        '''

        self.matrix = [[0 for j in range(vertices)] for i in range(vertices)]
        self.cost = [[0 for j in range(vertices)] for i in range(vertices)]
        self.v = vertices
        self.edges = []


    def add_edge(self, start_node, end_node, cost):

        '''
        Adds the edge for the matrix representation
        of the graph
        '''

        self.matrix[start_node][end_node] = 1
        self.cost[start_node][end_node] = cost

        self.edges.append((start_node, end_node))


    def print_cost(self):

        '''
        Used to print the cost matrix of the graph
        '''

        res = ""
        for item in self.cost:
            res += str(item) + "\n"
        return res


    def print_graph(self):

        '''
        Used to print the matrix representation of the graph
        '''

        res = ""
        for item in self.matrix:
            res += str(item) + "\n"
        return res


    def bellman_ford(self, start_node):

        '''
        Implementation of bellman ford algorithm
        '''

        table = [math.inf for i in range(self.v)]
        table[start_node] = 0

        for i in range(self.v - 1):
            for item in self.edges:
                if table[item[0]] + self.cost[item[0]][item[1]] < table[item[1]]:
                    table[item[1]] = table[item[0]] + self.cost[item[0]][item[1]]

        table_new = table.copy()
        for i in range(1):
            for item in self.edges:
                if table_new[item[0]] + self.cost[item[0]][item[1]] < table_new[item[1]]:
                    table_new[item[1]] = table_new[item[0]] + self.cost[item[0]][item[1]]

        if table_new == table:
            print('|-------|--------|')
            print('   Node |', 'Values')
            print('|-------|--------|')
            for ind in range(len(table)):
                print('   ', ind, '\t|  ', table[ind])
                print('|-------|--------|')
        else:
            print("Table values after (V - 1)th iteration")
            print("--------------------------------------")
            print()
            print('|-------|--------|')
            print('   Node |', 'Values')
            print('|-------|--------|')
            for ind in range(len(table)):
                print('   ', ind, '\t|  ', table[ind])
                print('|-------|--------|')
            print()

            print("\nTable values during (V)th iteration")
            print("-------------------------------------")
            print()
            print('|-------|--------|')
            print('   Node |', 'Values')
            print('|-------|--------|')
            for ind in range(len(table_new)):
                print('   ', ind, '\t|  ', table_new[ind])
                print('|-------|--------|')

            print('\nThe graph contains a cycle with negative edge')


if __name__ == '__main__':

    print("CASE - 1")
    print("--------")
    print()

    g = Graph(7)

    g.add_edge(0, 1, 6)
    g.add_edge(0, 2, 5)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 4, -1)
    g.add_edge(2, 1, -2)
    g.add_edge(3, 2, -2)
    g.add_edge(2, 4, 1)
    g.add_edge(4, 6, 3)
    g.add_edge(3, 5, -1)
    g.add_edge(5, 6, 3)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()
    print(g.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()
    print(g.print_cost())

    print("Result of Bellman ford algorithm")
    print("--------------------------------")
    print()
    g.bellman_ford(0)
    print()

    print("CASE - 2")
    print("--------")
    print()

    g = Graph(5)

    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()
    print(g.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()
    print(g.print_cost())

    print("Result of Bellman ford algorithm")
    print("--------------------------------")
    print()
    g.bellman_ford(0)
    print()

    print("CASE - 3")
    print("--------")
    print()

    g = Graph(4)

    g.add_edge(1, 0, 4)
    g.add_edge(0, 3, 5)
    g.add_edge(3, 2, 3)
    g.add_edge(2, 1, -10)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()
    print(g.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()
    print(g.print_cost())

    print("Result of Bellman ford algorithm")
    print("--------------------------------")
    print()
    g.bellman_ford(0)
    print()

    print("CASE - 4")
    print("--------")
    print()

    g = Graph(5)

    g.add_edge(3, 0, 4)
    g.add_edge(3, 2, 7)
    g.add_edge(3, 4, 3)
    g.add_edge(0, 2, 4)
    g.add_edge(2, 0, -9)
    g.add_edge(0, 4, 5)
    g.add_edge(4, 2, 3)
    g.add_edge(1, 2, -4)
    g.add_edge(4, 1, 2)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()
    print(g.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()
    print(g.print_cost())

    print("Result of Bellman ford algorithm")
    print("--------------------------------")
    print()
    g.bellman_ford(0)
    print()