import collections

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        if (False):
            window = ''
            for i,c in enumerate(s):
                print(i,window,c)
                if i==0:
                    window=c
                    continue
                elif c in window:
                    if window.index(c)==0:
                        window = window[1:]+c
                else:
                    window+=c
            return len("".join(set(window)))
        seq=''
        experiment = []
        str_len = len(s)

        for i,c in enumerate(s):
            print(i,c)
            if c in s[:i]:
                str_len = str_len - 1
                experiment.append(str_len)
            else:
                str_len = str_len + 1
                experiment.append(str_len)
        maxim = max(collections.Counter(experiment).items(), key=lambda k: k[1])
        print (experiment)
        return maxim[1]
print(Solution().lengthOfLongestSubstring("dvdkv"))