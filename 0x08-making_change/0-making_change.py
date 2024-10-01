#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): List of coin denominations available.
        total (int): The target total amount.
    Returns:
        int: The fewest number of coins needed to make the total,
        or -1 if it cannot be made.
    """
    if total <= 0:
        return 0

    # Initialize DP array, large value for unattainable totals, 0 for total 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make 0

    # Update the dp array with the minimum coins needed for each amount
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1 (impossible to make the total)
    return dp[total] if dp[total] != float('inf') else -1
