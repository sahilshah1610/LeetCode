class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 1
        for x in range(1, len(nums)+2):
            if x not in nums:
                return x


if __name__ == "__main__":
    objSolution = Solution()
    nums = [6,4,7,8]
    print(objSolution.firstMissingPositive(nums))