from collections import defaultdict
import ast

class Graph:

    '''
    Class Graph
    Data Members
        - matrix
        - cost
        - v
        - graph
        - visited_DFS
        - visited_BFS
        - queue
        - path_string
    Member Functions
        - add_edge
        - print_graph
        - print_cost
        - DFS
        - BFS
        - path_recur
        - paths
        - calculate_cost
    '''

    def __init__(self, vertices):

        '''
        Initialising values of the data members
        '''

        self.matrix = [[0 for j in range(vertices)] for i in range(vertices)]
        self.cost = [[0 for j in range(vertices)] for i in range(vertices)]
        self.v = vertices
        self.graph = defaultdict(list)

        self.visited_DFS = []
        self.visited_BFS = []
        self.queue = []
        self.path_string = ''


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

        self.graph[start_node].append(end_node)


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


    def BFS(self, start_node = 0):

        '''
        Returns the Breadth First Traversal
        of the graph
        '''

        self.visited_BFS.append(start_node)
        self.queue.append(start_node)

        while self.queue:

            node = self.queue.pop(0)

            for neighbour in self.graph[node]:
                if neighbour not in self.visited_BFS:
                    self.visited_BFS.append(neighbour)
                    self.queue.append(neighbour)

        return self.visited_BFS 
    
    
    def path_recur(self, u, d, visited, path):

        '''
        Spportive recursive function for paths function
        '''

        visited[u] = True
        path.append(u)

        if u == d:
            self.path_string += str(path) + '\n'
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.path_recur(i, d, visited, path)

        path.pop()
        visited[u] = False


    def paths(self, start_node, end_node):

        '''
        Returns the all the possible paths from
        start node to end node
        '''

        visited = [False] * (self.v)
        path = []
        self.path_recur(start_node, end_node, visited, path)

        path = self.path_string
        path = [ast.literal_eval(path) for path in path.split('\n') if path != '']

        return path
    

    def calculate_cost(self, start_node, end_node):

        '''
        Returns the optimal path along with
        the optimal cost
        '''

        path = g.paths(start_node, end_node)

        list_of_cost = []

        for item in path:

            cost = 0
            for ind in range(len(item) - 1):
                cost += self.cost[item[ind]][item[ind + 1]]

            list_of_cost.append(cost)

        optimal_path = list(zip(path, list_of_cost))
        optimal_path.sort(key = lambda item : item[1])

        return optimal_path[0]


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

    print("Breadth First Search : ")
    print("-----------------------")
    print(g.BFS())
    print()

    print("All possible paths from start node to end node : ")
    print("-------------------------------------------------")
    print(g.paths(0, 3))
    print()

    print("Optimal path and Cost : ")
    print("------------------------")
    print(g.calculate_cost(0, 3))
    print()

    print("CASE - 2")
    print("--------")
    print()

    g = Graph(5)

    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 3, 3)
    g.add_edge(1, 4, 4)

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

    print("Breadth First Search : ")
    print("-----------------------")
    print(g.BFS())
    print()

    print("All possible paths from start node to end node : ")
    print("-------------------------------------------------")
    print(g.paths(0, 3))
    print()

    print("Optimal path and Cost : ")
    print("------------------------")
    print(g.calculate_cost(0, 3))
    print()

    print("CASE - 3")
    print("--------")
    print()

    g = Graph(5)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(0, 3, 1)
    g.add_edge(1, 2, 5)
    g.add_edge(2, 4, 8)

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

    print("Breadth First Search : ")
    print("-----------------------")
    print(g.BFS())
    print()

    print("All possible paths from start node to end node : ")
    print("-------------------------------------------------")
    print(g.paths(0, 4))
    print()

    print("Optimal path and Cost : ")
    print("------------------------")
    print(g.calculate_cost(0, 4))
    print()