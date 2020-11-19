class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i<len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i +=1
        return len((nums))

if __name__ == "__main__":
    objsolution = Solution()
    nums = [0,0,1,1,1,2,2,3,4,3]
    print(objsolution.removeDuplicates(nums))