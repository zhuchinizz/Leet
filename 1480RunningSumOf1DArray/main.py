class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = []
        for i in range (len(nums)):
            if i == 0:
                sum.append(nums[i])
            else:
                sum.append(sum[i-1]+nums[i])
        return sum