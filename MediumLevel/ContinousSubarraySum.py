#done
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        i= 1
        while(i!=len(nums)):
            for x in range(i,len(nums)):
                print(nums[x-i:x+1])
                slidingWindowsum = sum(nums[x-i:x+1])
                try:
                    if slidingWindowsum%k==0:
                        return True
                except ZeroDivisionError:
                    if slidingWindowsum == 0:
                        return True
            i+=1

        return False


if __name__ == "__main__":
    nums = [23,2,6,4,7]
    k= 0
    objSol = Solution()
    print(objSol.checkSubarraySum(nums, k))


