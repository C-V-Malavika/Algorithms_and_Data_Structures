class Knapsack:

    '''
    Class Knapsack
    Data Members
        - M
        - sack
        - items
        - prof_weight
    Member Functions
        - add_item
        - approx_knapsack
    '''

    def __init__(self, weight):

        '''
        Initialising values of the data members
        '''

        self.M = weight
        self.sack = {}
        self.items = []
        self.prof_weight = {}

    
    def add_item(self, item, profit, weight):

        '''
        Getting the items, profits and weights
        '''

        self.sack[item] = (profit, weight)
        self.prof_weight[item] = profit / weight
        self.items.append(item)


    def approx_knapsack(self):

        '''
        Returns the sack with the items that can
        be accomodated using approximation algorithm
        '''

        sack = []
        self.prof_weight = sorted(self.prof_weight.items(), key = lambda item : item[1], reverse = True)
        sum_weight = 0
        item = self.prof_weight.pop(0)[0]

        while sum_weight + self.sack[item][1] <= self.M:

            sack.append(item)
            sum_weight += self.sack[item][1]
            item = self.prof_weight.pop(0)[0]
        
        return sack


if __name__ == '__main__':

    k = Knapsack(15)

    k.add_item('x1', 10, 2)
    k.add_item('x2', 10, 4)
    k.add_item('x3', 12, 6)
    k.add_item('x4', 18, 9)

    print(k.approx_knapsack())