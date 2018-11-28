class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def chack_palindrome(pstring):
            return pstring == pstring[::-1]

        for i,c in enumerate(s):
            for j, d in enumerate(s[i:]):
                print (j,d,s[i:j])

Solution().longestPalindrome("babad")