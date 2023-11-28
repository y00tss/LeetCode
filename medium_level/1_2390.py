"""
Note:
    !!! List.append is faster than string += string !!!


The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

"""
import time

start = time.perf_counter()


def removeStars(s: str) -> str:
    string = []
    for i in s:
        if i != '*':
            string.append(i)
            continue
        else:
            string.pop()
    return "".join(string)


finish = time.perf_counter()

s = 'leet**cod*e'
print(str(finish - start), removeStars(s))
