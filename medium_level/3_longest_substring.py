class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        longest_substring = 0
        unique_chars = []
        for i in range(len(s)):
            if s[i] not in unique_chars:
                unique_chars.append(s[i])
            else:
                if len(unique_chars) > longest_substring:
                    longest_substring = len(unique_chars)
                unique_chars = unique_chars[unique_chars.index(s[i])+1:]
                unique_chars.append(s[i])
        if len(unique_chars) > longest_substring:
            longest_substring = len(unique_chars)
        return longest_substring


