class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):
            if target - nums[x] in nums:
                secondValue = nums.index(target - nums[x])
                if secondValue != x:
                    return [ secondValue, x]


        # count = 0
        # while count != len(nums):
        #     for x in range(len(nums)):
        #         if x!=count:
        #             if nums[x]+nums[count] == target:
        #                 result.append(count)
        #                 result.append(x)
        #                 return result
        #     count+=1

if __name__ == "__main__":
    objSolution = Solution()
    nums = [3,2,3]
    target = 6
    print(objSolution.twoSum(nums, target))