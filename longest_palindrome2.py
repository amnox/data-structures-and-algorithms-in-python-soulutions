class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def check_palindrome(pstring):
            return pstring == pstring[::-1]
        max_palin = ''
        s_len = len(s)
        for i,c in enumerate(s):
            cur_s = s[i:]
            for j, d in enumerate(cur_s):
                if (len(cur_s[:j+1])>len(max_palin)):
                    if(check_palindrome(cur_s[:j+1])):
                        max_palin = cur_s[:j+1]
                else:
                    continue
        print(max_palin)

Solution().longestPalindrome("nypdmqqgauepeyfvwcdpbmmaxfwxmmtswfuwldtvqcisywalfnvovuordczxlyzqmslxilpnenbuwbcpebneovitwkkswsijajnkwkfbxnulmwotgrmpklntfyjavccbrgwqynryeoswmhsqzcwnudkuvfkikjxjkjpghsytjfkpvkjpvblamdeegeohospporbtorkbuggbawgodhxpscfksjbirxvjyjapwwushmnqsxktnslvonlwvuseinrmwvfqjgzpkwcqfzfdbbmcngmsoeegudwjvldqmaomwbqvijesnpxiqvtfeiqebrfjhtvjdwkopyfzaslewdjnkmalvfinbuouwcgnfecjtdzwycxrynxepbcsroyzrsgiiuaszvatwyuxinwhni")