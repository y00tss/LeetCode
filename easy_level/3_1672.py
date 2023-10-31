'''
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
'''


def maximumWealth(accounts: list) -> int:
    max_wealth = 0
    for items in accounts:
        if sum(items) > max_wealth:
            max_wealth = sum(items)
    return max_wealth


print(maximumWealth([[1, 5], [7, 3], [3, 5]]))
