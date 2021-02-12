from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        if len(nums) <=2:
            return output

        # for x in range( len(nums)-2):
        #     for y in range(1, len(nums)-1):
        #         for z in range(2, len(nums)):
        #             print(x, y, z)
        #             if x!=y and y!=z and z!=x:
        #                 if nums[x] + nums[y] + nums[z] ==0:
        #                     print(x, y, z)
        #                     output.append([nums[x], nums[y], nums[z]])
        nums.sort()
        output = []

        for i in range(len(nums)-2):

            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while(left<right):
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left = left+1
                elif sum >0:
                    right = right-1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left +=1
                    while left<right and nums[right]==nums[right-1]:
                        right -=1
                    left = left+1
                    right =right-1

        return output



if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    #nums = [-4 ,-1, -1, 0, 1, 2]
    objSol = Solution()
    print(objSol.threeSum(nums))