from collections import defaultdict

class StableMarriage:

    '''
    Class StableMarriage
    Data Members
        - n
        - men_preference
        - women_preference
        - pref_matrix
        - pair
    Member Functions
        - add_men_preference
        - add_women_preference
        - preference_matrix
        - stable_marriage
    '''

    def __init__(self, n):

        '''
        Initialises the values of the data members
        '''

        self.n = n
        self.men_preference = defaultdict(list)
        self.women_preference = defaultdict(list)
        self.pref_matrix = {}
        self.pair = {}


    def add_men_preference(self, men, women):

        '''
        Adds women to the men's preference matrix
        '''

        self.men_preference[men].append(women)


    def add_women_preference(self, women, men):

        '''
        Adds men to the women's preference matrix
        '''

        self.women_preference[women].append(men)


    def preference_matrix(self):

        '''
        Computes the preference matrix
        '''

        for men in self.men_preference:
            for women in self.women_preference:
                self.pref_matrix[(men, women)] = [self.men_preference[men].index(women) + 1, self.women_preference[women].index(men) + 1]

        return self.pref_matrix


    def stable_marriage(self):

        '''
        Returns the stable marriage pairs
        '''

        for men in self.men_preference:
            self.pair[men] = 'free'

        lst_pref = self.preference_matrix()
        free_men = [item for item in self.pair if self.pair[item] == 'free']

        while free_men != []:

            for man in free_men:

                for woman in self.men_preference[man]:
                    if self.pair[man] == 'free' and woman not in self.pair.values():
                        self.pair[man] = woman

                    elif woman in self.pair.values():
                        for pm in self.pair:
                            if self.pair[pm] == woman:
                                paired_man = pm

                        d = {item  : lst_pref[item] for item in lst_pref if item[1] == woman}

                        if d[(man, woman)][1] >= d[(paired_man, woman)][1]:
                            self.pair[paired_man] = woman
                        else:
                            self.pair[paired_man] = 'free'
                            self.pair[man] = woman

                free_men = [item for item in self.pair if self.pair[item] == 'free']

        return self.pair


if __name__ == '__main__':

    print("CASE - 1")
    print("--------")
    print()

    s = StableMarriage(3)

    s.add_men_preference('Bob', 'Lea')
    s.add_men_preference('Bob', 'Ann')
    s.add_men_preference('Bob', 'Sue')
    s.add_men_preference('Jim', 'Lea')
    s.add_men_preference('Jim', 'Sue')
    s.add_men_preference('Jim', 'Ann')
    s.add_men_preference('Tom', 'Sue')
    s.add_men_preference('Tom', 'Lea')
    s.add_men_preference('Tom', 'Ann')

    s.add_women_preference('Ann', 'Jim')
    s.add_women_preference('Ann', 'Tom')
    s.add_women_preference('Ann', 'Bob')
    s.add_women_preference('Lea', 'Tom')
    s.add_women_preference('Lea', 'Bob')
    s.add_women_preference('Lea', 'Jim')
    s.add_women_preference('Sue', 'Jim')
    s.add_women_preference('Sue', 'Tom')
    s.add_women_preference('Sue', 'Bob')

    print("STABLE MARRIAGE PAIRS")
    print("---------------------")

    for item in s.stable_marriage():
        print(item, '-->', s.stable_marriage()[item])
    print()

    print("CASE - 2")
    print("--------")
    print()

    s = StableMarriage(3)

    s.add_men_preference('M1', 'W2')
    s.add_men_preference('M1', 'W1')
    s.add_men_preference('M1', 'W3')
    s.add_men_preference('M2', 'W2')
    s.add_men_preference('M2', 'W3')
    s.add_men_preference('M2', 'W1')
    s.add_men_preference('M3', 'W3')
    s.add_men_preference('M3', 'W1')
    s.add_men_preference('M3', 'W2')

    s.add_women_preference('W1', 'M1')
    s.add_women_preference('W1', 'M2')
    s.add_women_preference('W1', 'M3')
    s.add_women_preference('W2', 'M2')
    s.add_women_preference('W2', 'M3')
    s.add_women_preference('W2', 'M1')
    s.add_women_preference('W3', 'M3')
    s.add_women_preference('W3', 'M1')
    s.add_women_preference('W3', 'M2')

    print("STABLE MARRIAGE PAIRS")
    print("---------------------")

    for item in s.stable_marriage():
        print(item, '-->', s.stable_marriage()[item])