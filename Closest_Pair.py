class Point:

    '''
    Class Point
    Data Members :
        - x (x - coordinate)
        - y (y - coordinate)
    Member Functions :
        - euclidean_distance
        - __str__
    '''

    def __init__(self, x, y):

        '''
        Initialising the vales of the data members
        '''

        self.x = x
        self.y = y


    def euclidean_distance(self, other):

        '''
        Computes the euclidean distance between
        two Point objects
        '''

        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5


    def __str__(self):

        '''
        For printing the Point object in the form
        of a string
        '''

        return f"({self.x}, {self.y})"


def closest(P, n):

    '''
    Firstly, sorts the input list 'P' with respect to
    x - coordinate of the points in 'P' and then
    calls the function 'closest_pair'
    '''

    P = sorted(P, key = lambda point: point.x)

    return closest_pair(P, n)


def base_condition(P, n):

    '''
    Serves as the base condition for the
    closest_pair recursive function

    If the list 'P' has 2 points, return the distance between
    the two points

    If the list 'P' has 3 points, return the minimum distance
    between the 3 possible pairs (without repetition)
    '''

    if (n == 2):
        return P[0].euclidean_distance(P[1])

    if (n == 3):
        return min(P[0].euclidean_distance(P[1]), P[1].euclidean_distance(P[2]), P[0].euclidean_distance(P[2]))


def closest_pair(P, n):

    '''
    If the value of n is less than or equal to 3
    'base_condition' is invoked

    Otherwise, mid point is found and the list 'P'
    if split into two parts - dleft and d_right
    and minimum distance among them is taken
    and stored in the variable 'dist'.

    Strip region is calculated and the minimum of strip
    region and 'dist' is computed
    '''

    if n <= 3:
        return base_condition(P, n)

    mid = n // 2
    mid_point = P[mid]

    dleft = closest_pair(P, mid)
    dright = closest_pair(P[mid:], n - mid)
    dist = min(dleft, dright)

    strip = []

    for i in range(n):
        if abs(P[i].x - mid_point.x) < dist:
            strip.append(P[i])

    return min(dist, strip_closest(strip, len(strip), dist))


def strip_closest(strip, size, d):

    '''
    The points in the strip region are sorted
    with respect to y - coordinate of the points

    If there is any two points in 'strip' whose distance
    is less than 'min_dist', that distance is concluded to
    be the final result
    '''

    min_dist = d
    strip = sorted(strip, key = lambda point: point.y)

    for i in range(size):
        for j in range(i+1, size):
            if (strip[j].y - strip[i].y) >= min_dist:
                break
            if strip[i].euclidean_distance(strip[j]) < min_dist:
                min_dist = strip[i].euclidean_distance(strip[j])

    return min_dist


if __name__ == '__main__':

    import random
    import matplotlib.pyplot as plt

    list_of_points = []
    lst  = []

    i = 1

    while (i <= 500):
        x = round(random.uniform(1, 10), 2) # Random float values
        y = round(random.uniform(1, 10), 2) # Random float values

        # To avoid repetition of points in the list
        flag = 1
        for item in lst:
            if (item[0] == x and item[1] == y):
                flag = 0

        if flag == 1:
            lst.append([x, y])
            list_of_points.append(Point(x, y))
            i += 1

    print("List of points generated : ")
    print("---------------------------")
    for item in list_of_points:
        print(item)
        plt.plot(item.x, item.y, marker = 'o', color = 'red')
    print()

    print("Closed Pair has distance : ", closest(list_of_points, len(list_of_points)))
    print()

    plt.show()