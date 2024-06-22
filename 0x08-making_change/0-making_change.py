#!/usr/bin/python3
"""Defines a makeChange function."""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to make change for total.

    Args:
        coins: A list of the values of the coins in your possession.
        total: An integer representing the total to make change for.

    Returns:
        Fewest number of coins needed to make change for total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total %= coin
    return num_coins
