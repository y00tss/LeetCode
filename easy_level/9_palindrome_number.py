class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        try:
            return str(x) == str(x)[::-1]
        except:
            return False