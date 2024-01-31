"""
https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
"""


def reverseVowels(self, s):
    str_index = []
    vowel = []
    res = []
    pos = -1
    for index, value in enumerate(s):
        if value in 'aeiouAEIOU':
            str_index.append(-1)
            vowel.append(value)
        else:
            str_index.append(index)
    for index in str_index:
        if index < 0:
            res.append(vowel[pos])
            pos -= 1
        else:
            res.append(s[index])
    return ''.join(res)