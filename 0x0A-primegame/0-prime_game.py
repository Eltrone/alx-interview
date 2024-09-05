#!/usr/bin/python3


def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes


def isWinner(x, nums):
    from functools import lru_cache

    @lru_cache(None)
    def can_win(n):
        primes = sieve_of_eratosthenes(n)
        if not primes:
            return False
        for prime in primes:
            if not can_win(n - prime):
                return True
        return False

    maria_wins = 0
    for n in nums:
        if can_win(n):
            maria_wins += 1

    ben_wins = x - maria_wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    x = int(input("Enter the number of rounds: "))
    nums_input = input("Enter the list of numbers for each round: ")
    nums = list(map(int, nums_input.split()))
    print("Winner: {}".format(isWinner(x, nums)))
