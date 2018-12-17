'''
- Till master array empty
-- Drain Top Array
-- pop last element from last till n-1
-- Drain last in reverse
-- pop first till second index



'''


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        master_spiral = []
        if len(matrix)==0:
            return []
        if len(matrix[0])==1:
            for aa in matrix:
                master_spiral.extend(aa)
            return master_spiral
        if len(matrix[0])==2:
            while len(matrix) > 0:
                first_row = matrix.pop(0)
                master_spiral.extend(first_row)
                for i, element in enumerate(matrix):
                    if len(matrix[0])==0:
                        break
                    if i == len(matrix) - 1:
                        last_list = matrix.pop()
                        master_spiral.extend(last_list[::-1])
                        break
                    master_spiral.append(element.pop())
                for i, element in enumerate(matrix[::-1]):
                    if len(matrix[0])==0:
                        break
                    if i == len(matrix) - 1:
                        break
                    master_spiral.append(element.pop())
            return master_spiral
        while len(matrix)>0:
            first_row = matrix.pop(0)
            master_spiral.extend(first_row)
            for i, element in enumerate(matrix):
                if i == len(matrix)-1:
                    last_list = matrix.pop()
                    master_spiral.extend(last_list[::-1])
                    break
                master_spiral.append(element.pop())
            for i, element in enumerate(matrix[::-1]):
                if i == len(matrix)-1:
                    break
                master_spiral.append(element.pop())

        return(master_spiral)
ass = Solution().spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])

print(ass)