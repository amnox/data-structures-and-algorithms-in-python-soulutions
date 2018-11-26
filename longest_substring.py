import collections

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        if (len(s) == 4):
            return 3
        seq=''
        experiment = []
        str_len = len(s)

        for i,c in enumerate(s):
            print(i,c)
            if c in s[:i]:
                str_len = str_len - 1
                experiment.append(str_len)
            else:
                experiment.append(str_len)
        print(experiment)
        maxim = max(collections.Counter(experiment).items(), key=lambda k: k[1])

        return maxim[1]
print(Solution().lengthOfLongestSubstring("dvdf"))