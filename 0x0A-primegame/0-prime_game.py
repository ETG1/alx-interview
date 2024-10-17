#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(rounds: int, numbers: list) -> str:
    """Determines the winner of the prime game.

    Args:
    rounds (int): The number of rounds.
    numbers (list): A list of numbers.

    Returns:
    str: The winner of the game, either "Ben" or "Maria"
    or None if the input is invalid.
    """
    if rounds <= 0 or numbers is None or rounds != len(numbers):
        return None

    ben_score = 0
    maria_score = 0

    prime_flags = [True] * (max(numbers) + 1)
    prime_flags[0] = prime_flags[1] = False

    for num in range(2, int(max(numbers) ** 0.5) + 1):
        if prime_flags[num]:
            for multiple in range(num * num, max(numbers) + 1, num):
                prime_flags[multiple] = False

    for num in numbers:
        if sum(prime_flags[:num + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    else:
        return None
