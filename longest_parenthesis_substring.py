class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        OPEN = '('
        CLOSE = ')'
        contendor = 0
        def check_valid(strr):
            if len(strr) == 0:
                return False
            pop_art = []
            for s in strr:
                if len(pop_art) == 0:
                    pop_art.append(s)
                    continue
                if pop_art[-1] == OPEN and s == CLOSE:
                    pop_art.pop()
                    continue
                else:
                    pop_art.append(s)
            return len(pop_art) == 0
        for i, str_i in enumerate(s):
            #print ('-',i,str_i,s[i:])
            if str_i == CLOSE:
                continue
            for j, str_j in enumerate(s[i:]):
                #if check_valid(s[:j]):
                    #print('--', j,s[:j],check_valid(s[:j]))
                shitt = s[i:]
                #print(i,j, shitt[:j+1], check_valid(shitt[:j+1]))
                if check_valid(shitt[:j+1]):
                    if contendor<len(shitt[:j+1]):
                        contendor = len(shitt[:j+1])
        #print(contendor)
        return contendor

Solution().longestValidParentheses("(()(((((((((()))")