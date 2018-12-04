class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combos = 0
        visited = []
        bauss = []
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums):
                if i == j:
                    continue
                for k, num_k in enumerate(nums):
                    if k == i or k == j:
                        continue
                    if sorted([num_i, num_j, num_k]) in visited:
                        #print("exclude ", set([num_i, num_j, num_k]))
                        continue
                    visited.append(sorted([num_i, num_j, num_k]))
                    #print([i, j, k], [num_i, num_j, num_k])
                    if sum([num_i, num_j, num_k]) == 0:
                        bauss.append([num_i, num_j, num_k])
        #print(combos)
        return(bauss)


Solution().threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0])

arrerr = [[0, 1, 2],[-1, 0, 1],[0, 1, 3],[-1, 0, 2],[0, 1, 4],[-1, 0, -1],[0, 1, 5],[-1, 0, -4],[0, 2, 1],[-1, 1, 0],[0, 2, 3],[-1, 1, 2],[0, 2, 4],[-1, 1, -1],[0, 2, 5],[-1, 1, -4]]
sett = []
for shit in arrerr:
    sett.append(set(shit))

