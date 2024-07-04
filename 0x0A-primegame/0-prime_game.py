#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Returns name of the player that wins the most rounds"""
    if not nums or x < 1:
        return None

    # sieve of Eratosthenes (set all numbers as prime)
    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]

    primes[0], primes[1] = False, False  # 0 and 1 are not prime

    # set multiples of primes as not prime
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    primes_count = [0 for _ in range(len(primes))]
    count = 0

    # count primes
    for i in range(len(primes)):
        if primes[i]:
            count += 1
        primes_count[i] = count

    player1 = 0
    for n in nums:
        player1 += primes_count[n] % 2 == 1

    if player1 * 2 == len(nums):
        return None

    if player1 * 2 > len(nums):
        return "Maria"

    return "Ben"
