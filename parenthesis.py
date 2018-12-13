from itertools import combinations


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        OPEN = '('
        CLOSE = ')'

        def check_valid(strr):
            queye = [strr.pop(0)]
            if queye[0] == CLOSE:
                return False
            while len(strr) > 0:
                if len(queye) == 0:
                    queye.append(strr.pop())
                curr = strr.pop(0)

                if curr == queye[0]:
                    queye.append(curr)
                else:
                    queye.pop()
            return len(queye) == 0

        smash_str = []
        for i in range(0, n):
            smash_str.append(OPEN)
            smash_str.append(CLOSE)

        def permutations_with_repetition(s):
            base = len(s)
            liss = []
            for n in range(base ** base):
                yield [s[n // base ** (base - d - 1) % base] for d in range(base)]

        sauce = []
        perr = [list(s) for s in combinations(''.join(smash_str), len(smash_str))]
        print(combinations(smash_str,2))
        for p in perr:
            print(p)

        return sauce
Solution().generateParenthesis(5)