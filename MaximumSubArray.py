from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = nums[0]
        totalSum =0
        for x in nums:
            if totalSum<0:
                totalSum = 0
            totalSum +=x
            maxValue = max(totalSum, maxValue)
        return maxValue





if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    objSol = Solution()
    print(objSol.maxSubArray(arr))