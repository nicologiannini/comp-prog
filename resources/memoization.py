# A little overview of memoization


def fib(n):
    """ Simple method for Fibonacci Sequence """
    if n is 1:
        return 0
    if n is 2 or n is 3:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_memo(n, memo={}):
    """ Memoized version """
    if n in memo:
        return memo[n]
    if n is 1:
        return 0
    if n is 2 or n is 3:
        return 1
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


print(fib_memo(1))
print(fib_memo(3))
print(fib_memo(8))
print(fib_memo(50))


def grid_traveler(m, n):
    """ Simple method to find how many paths are in a m x n grid 
    from (1, 1) to (m, n) while being able to move only down or right """
    if m is 1 and n is 1:
        return 1
    if m is 0 or n is 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


def grid_traveler_memo(m, n, memo={}):
    key = f"{m},{n}"
    if key in memo:
        return memo[key]
    if m is 1 and n is 1:
        return 1
    if m is 0 or n is 0:
        return 0
    memo[key] = grid_traveler_memo(m - 1, n, memo) + grid_traveler_memo(m, n - 1, memo)
    return memo[key]


print(grid_traveler_memo(1, 1))
print(grid_traveler_memo(2, 3))
print(grid_traveler_memo(3, 4))
print(grid_traveler_memo(18, 18))
