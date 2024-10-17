#!/usr/bin/python3


def sieve_of_eratosthenes(max_n):
    """ Generate a list indicating prime numbers up to max_n. """
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False
    return primes


def count_primes_up_to_n(n, primes):
    """ Count the number of primes up to and including n. """
    return sum(primes[2:n + 1])


def isWinner(x, nums):
    """ Determine who wins the most rounds between Maria and Ben. """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to_n(n, primes)

        # Maria starts first, so if the number of primes is odd,
        # Maria wins, otherwise Ben wins.
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
