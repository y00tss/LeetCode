"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1161833866/?envType=study-plan-v2&envId=leetcode-75
"""


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]


candies = [2, 3, 5, 1, 3]
extraCandies = 3

print(kidsWithCandies(candies, extraCandies))

"""
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
"""
