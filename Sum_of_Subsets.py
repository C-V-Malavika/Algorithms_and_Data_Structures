class SumofSubset:

    '''
    Class SumofSubset
    Data Members
        - flag
    Member Functions
        - print_subset_sum
    '''

    def __init__(self):

        '''
        Initialises the values of the data members
        '''

        self.flag = False

 
    def print_subset_sum(self, i, n, lst, target_sum, subset):

        '''
        Returns the subsets whose sum equals the target sum
        '''

        if target_sum == 0:

            self.flag = True
            print("[", end=" ")
            for element in subset:
                print(element, end=" ")
            print("]", end="")
            return
    
        if i == n:

            return

        self.print_subset_sum(i + 1, n, lst, target_sum, subset)
    
        if lst[i] <= target_sum:

            subset.append(lst[i])
    
            self.print_subset_sum(i + 1, n, lst, target_sum - lst[i], subset)
    
            subset.pop()
 

if __name__ == "__main__":

    print("CASE 1")
    print("------")

    s = SumofSubset()
    s.print_subset_sum(0, len([1, 2, 1]), [1, 2, 1], 3, [])
    if not s.flag:
        print("There is no such subset")
    print()
    print()

    print("CASE 2")
    print("------")

    s = SumofSubset()
    s.print_subset_sum(0, len([3, 34, 4, 12, 5, 2]), [3, 34, 4, 12, 5, 2], 30, [])
    if not s.flag:
        print("There is no such subset")