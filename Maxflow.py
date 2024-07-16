import ast
from collections import defaultdict

class MaxFlow:

    def __init__(self, vertices):

        '''
        Initialises the values of the data members
        '''

        self.v = vertices
        self.matrix = [[0 for j in range(vertices)] for i in range(vertices)]
        self.cost = [[0 for j in range(vertices)] for i in range(vertices)]
        self.graph = defaultdict(list)
        self.residual_graph = {}
        self.path_string = ""


    def add_edge(self, start_node, sink_node, cost):

        '''
        Adds the edge for the matrix representation
        of the graph
        '''

        self.matrix[start_node][sink_node] = 1
        self.cost[start_node][sink_node] = cost
        self.graph[start_node].append(sink_node)
        self.residual_graph[(start_node, sink_node)] = [0, cost]


    def print_graph(self):

        '''
        Used to print the matrix representation of the graph
        '''
        
        res = ""
        for item in self.matrix:
            res += str(item) + "\n"
        
        return res


    def print_cost(self):

        '''
        Used to print the cost matrix of the graph
        '''
        
        res = ""
        for item in self.cost:
            res += str(item) + "\n"
        
        return res
    

    def path_recur(self, u, d, visited, path):

        '''
        Spportive recursive function for augmented_paths function
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


    def augmented_paths(self, start_node, sink_node):

        '''
        Returns the all the possible paths from
        start node to end node
        '''

        visited = [False] * (self.v)
        path = []
        self.path_recur(start_node, sink_node, visited, path)

        path = self.path_string
        path = [ast.literal_eval(path) for path in path.split('\n') if path != '']
    
        return path   
    

    def select_augmented_path(self, start_node, sink_node, augmented_paths):

        '''
        Selects the feasible augmented path from all possible
        augmented paths
        '''

        try:
            augmented_path = augmented_paths.pop(0)
        except IndexError:
            return []
        Flag = False

        for index in range(len(augmented_path) - 1):
            if self.residual_graph[augmented_path[index], augmented_path[index + 1]][0] == self.residual_graph[augmented_path[index], augmented_path[index + 1]][1] or \
                self.residual_graph[augmented_path[index], augmented_path[index + 1]][0] == self.residual_graph[augmented_path[index], augmented_path[index + 1]][-1]:
                Flag = True
                break

        if Flag == True:
            return self.select_augmented_path(start_node, sink_node, augmented_paths)
        else:
            return augmented_path
        

    def max_flow(self, start_node, sink_node):

        '''
        Returns the max flow of the given graph
        '''
        
        cost = []
        max_flow = 0

        augmented_path = [0]

        while augmented_path != []:

            augmented_path = self.select_augmented_path(start_node, sink_node, self.augmented_paths(start_node, sink_node))
            if augmented_path == []:
                return max_flow
    
            for index in range(len(augmented_path) - 1):
                cost.append(self.residual_graph[augmented_path[index], augmented_path[index + 1]][1])
            min_of_space = min(cost)

            for index in range(len(augmented_path) - 1):
                self.residual_graph[augmented_path[index], augmented_path[index + 1]][0] += min_of_space
            max_flow += min_of_space

        return max_flow
    

if __name__ == '__main__':

    print("CASE - 1")
    print("--------")
    print()

    m = MaxFlow(4)

    m.add_edge(0, 1, 2)
    m.add_edge(0, 2, 1)
    m.add_edge(1, 3, 1)
    m.add_edge(1, 2, 3)
    m.add_edge(2, 3, 2)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()

    print(m.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()

    print(m.print_cost())

    print("The residual graph is")
    print("---------------------")
    print()

    print(m.residual_graph)
    print()

    print("Max Flow")
    print("--------")
    print()

    print(m.max_flow(0, 3))
    print()

    print("CASE - 2")
    print("--------")
    print()

    m = MaxFlow(6)

    m.add_edge(0, 1, 16)
    m.add_edge(0, 2, 13)
    m.add_edge(1, 2, 10)
    m.add_edge(1, 3, 12)
    m.add_edge(2, 1, 4)
    m.add_edge(2, 4, 14)
    m.add_edge(3, 5, 20)
    m.add_edge(4, 3, 7)
    m.add_edge(4, 5, 4)
    
    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()

    print(m.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()

    print(m.print_cost())

    print("The residual graph is")
    print("---------------------")
    print()

    print(m.residual_graph)
    print()

    print("Max Flow")
    print("--------")
    print()

    print(m.max_flow(0, 5))
    print()
    
    print("CASE - 3")
    print("--------")
    print()

    m = MaxFlow(6)

    m.add_edge(0, 1, 7)
    m.add_edge(0, 4, 4)
    m.add_edge(1, 2, 5)
    m.add_edge(1, 3, 3)
    m.add_edge(2, 5, 8)
    m.add_edge(3, 2, 3)
    m.add_edge(3, 5, 5)
    m.add_edge(4, 3, 2)
    m.add_edge(4, 1, 3)

    print("The matrix representation of the graph is")
    print("-----------------------------------------")
    print()

    print(m.print_graph())

    print("The cost matrix representation of the graph is")
    print("----------------------------------------------")
    print()

    print(m.print_cost())

    print("The residual graph is")
    print("---------------------")
    print()

    print(m.residual_graph)
    print()

    print("Max Flow")
    print("--------")
    print()

    print(m.max_flow(0, 5))