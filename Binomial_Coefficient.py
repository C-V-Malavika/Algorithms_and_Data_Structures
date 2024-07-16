def binomial_expansion(n, a, b):

    '''
    To compute binomial coefficient table
    and the expansion of (a + b)^n
    '''

    list_binomial_coefficient = [[None for j in range(n + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(i + 1):
            if ((j == 0) or (i == j)):
                list_binomial_coefficient[i][j] = 1
            else:
                list_binomial_coefficient[i][j] = list_binomial_coefficient[i - 1][j - 1] + list_binomial_coefficient[i - 1][j]

    print("BINOMIAL COEFFICIENT TABLE\n")
    print(list_binomial_coefficient)
    print()

    a_temp = a ** n
    b_temp = 1
    result_sum = 0

    for i in range(n + 1):

        result_sum += list_binomial_coefficient[n][i] * a_temp * b_temp
        a_temp //= a
        b_temp *= b

    return result_sum


if __name__ == '__main__':

    print("CASE - 1")
    print("--------")
    print()

    n = 10
    a = 100
    b = 2
    print(f"({a} + {b}) ^ {n} =", binomial_expansion(n, a, b))
    print()

    print("CASE - 2")
    print("--------")
    print()

    n = 5
    a = 8
    b = 2
    print(f"({a} + {b}) ^ {n} =", binomial_expansion(n, a, b))
    print()

    print("CASE - 3")
    print("--------")
    print()

    n = 4
    a = 2
    b = 1
    print(f"({a} + {b}) ^ {n} =", binomial_expansion(n, a, b))