class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNums = list(set(nums))
        if len(setNums)>=3:
            setNums.pop(setNums.index(max(setNums)))
            setNums.pop(setNums.index(max(setNums)))
        return max(setNums)

if __name__ == "__main__":
    nums = [3,2,2,1]
    objSol = Solution()
    print(objSol.thirdMax(nums))