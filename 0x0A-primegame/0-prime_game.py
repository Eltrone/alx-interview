#!/usr/bin/python3
"""
Module for the Prime Game simulation where Maria and Ben play a game involving prime numbers.
"""

def sieve_of_eratosthenes(n):
    """Return a list of prime numbers up to n using the Sieve of Eratosthenes algorithm."""
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if prime[p]]

def isWinner(x, nums):
    """Determines the winner of the game based on prime number strategies.
    
    Args:
        x (int): Number of rounds.
        nums (list): List of upper limits for each round.
        
    Returns:
        str: 'Maria' if Maria wins more rounds, 'Ben' if Ben wins more rounds, None if it's a draw.
    """
    if x <= 0:
        return None

    primes = sieve_of_eratosthenes(max(nums)) if nums else []

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_moves = 0
        available = [True] * (n + 1)
        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                prime_moves += 1
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False

        if prime_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    x = int(input("Enter the number of rounds: "))
    nums = list(map(int, input("Enter the list of numbers for each round: ").split()))
    print("Winner: {}".format(isWinner(x, nums)))
