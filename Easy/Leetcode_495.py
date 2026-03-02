class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        max = 0

        for i in range(len(nums)):
            if nums[i] ==1:
                current = current + 1

                if current > max:
                    max = current
            else:
                current = 0
            
        return max
    