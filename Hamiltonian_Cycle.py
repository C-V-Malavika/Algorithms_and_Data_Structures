class Graph:

    '''
    Class Graph
    Data Members
        - matrix
        - v
        - has_cycle
    Member Functions
        - add_edge
        - print_graph
        - is_safe      
        - ham_cycle
        - hamiltonian
    '''

    def __init__(self, vertices):

        '''
        Initialising values of the data members
        '''

        self.v = vertices
        self.matrix = [[0 for j in range(self.v)] for i in range(self.v)]
        self.has_cycle = False

    
    def add_edge(self, start_node, end_node):

        '''
        Adds an edge to the matrix representation
        of the graph
        '''

        self.matrix[start_node][end_node] = 1
        self.matrix[end_node][start_node] = 1

    
    def print_graph(self):

        '''
        Displays the matrix representation
        of the graph
        '''

        res = ""
        for item in self.matrix:
            res += str(item) + "\n"
        return res
    

    def is_safe(self, v, path, pos):

        '''
        Returns False if the vertex is adjacent
        to the vertex which was previouly added or
        if was already included in the path,
        otherwise return True
        '''
    
        if self.matrix[path[pos - 1]][v] == 0:
            return False
    
        for i in range(pos):
            if path[i] == v:
                return False

        return True
 

    def ham_cycle(self):

        '''
        Finds whether hamiltonian
        cycle is possible or not and if
        possible finds all the hamiltonian
        cycles
        '''

        self.has_cycle = False
    
        path = []
        path.append(0)
    
        visited = [False] * (len(self.matrix))
    
        for i in range(len(visited)):
            visited[i] = False
    
        visited[0] = True
    
        self.hamiltonian(1, path, visited)
    
        if self.has_cycle == False:

            print("No Hamiltonian Cycle possible ")
            return
            
 
    def hamiltonian(self, pos, path, visited):

        '''
        Prints all the hamiltonian cycles of the
        given graph
        '''
    
        if pos == len(self.matrix):
        
            if self.matrix[path[-1]][path[0]] != 0:
            
                path.append(0)
                for i in range(len(path)):
                    if i != len(path) - 1:
                        print(path[i], end = " - ")
                    else:
                        print(path[i], end = " ")
                print()
    
                path.pop()
                self.has_cycle = True

            return
    
        for v in range(len(self.matrix)):
        
            if self.is_safe(v, path, pos) and not visited[v]:
                path.append(v)
                visited[v] = True
    
                self.hamiltonian(pos + 1, path, visited)
    
                visited[v] = False
                path.pop()


if __name__ == '__main__':

    print("CASE - 1")
    print("--------")
    print()

    g = Graph(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 1)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 3)
    g.add_edge(4, 5)

    g.ham_cycle()
    print()

    print("CASE - 2")
    print("--------")
    print()

    g = Graph(6)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    g.ham_cycle()