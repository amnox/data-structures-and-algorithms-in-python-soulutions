class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(0, target + 1):
            second = target - i
            if i in nums and second in nums:
                if i == second:
                    indices = [i2 for i2, x in enumerate(nums) if x == i]
                    return indices[:2]
                return [nums.index(i), nums.index(second)]

