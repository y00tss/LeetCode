"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1161827304/?envType=study-plan-v2&envId=leetcode-75
"""


def gcdOfStrings(self, str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return str1[:gcd(len(str1), len(str2))]

str1 = "LEET"
str2 = "CODE"

print(gcdOfStrings(str1, str2))
