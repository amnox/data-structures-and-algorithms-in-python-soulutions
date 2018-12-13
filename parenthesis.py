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


        class unique_element:
            def __init__(self, value, occurrences):
                self.value = value
                self.occurrences = occurrences


        def perm_unique(elements):
            eset=set(elements)
            listunique = [unique_element(i, elements.count(i)) for i in eset]
            u=len(elements)
            return perm_unique_helper(listunique, [0]*u, u-1)


        def perm_unique_helper(listunique, result_list, d):
            if d < 0:
                yield tuple(result_list)
            else:
                for i in listunique:
                    if i.occurrences > 0:
                        result_list[d]=i.value
                        i.occurrences-=1
                        for g in  perm_unique_helper(listunique, result_list, d-1):
                            yield g
                        i.occurrences+=1


        a = list(list(x) for x in perm_unique(smash_str) if x[0]!=')')
        return([x for x in a if check_valid(x)])
Solution().generateParenthesis(3)




