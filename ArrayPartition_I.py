from typing import List
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for x in range(len(nums)//2):
            sum+=nums[2*x]
        return sum


if __name__ == "__main__":
    nums = [6,2,6,5,1,2]
    objSol = Solution()
    print(objSol.arrayPairSum(nums))