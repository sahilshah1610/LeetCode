from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxValue = 0
        i=0
        j=1
        while(i!=len(nums)-1):
            product = (nums[i]-1) * (nums[j]-1)
            if product > maxValue:
                maxValue = product
            if j!= len(nums)-1:
                j+=1
            else:
                i+=1
                j=i+1
        
        return maxValue

if __name__ == "__main__":
    nums= [3,7]
    objSol = Solution()
    print(objSol.maxProduct(nums))