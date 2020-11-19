class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg, end = 0, len(nums)
        while beg < end:
            mid = (beg + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
        return beg

if __name__ == "__main__":
    objSolution = Solution()
    nums = [1,3,5,6]
    target = 7
    print(objSolution.searchInsert(nums, target))