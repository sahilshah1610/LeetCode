class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumDict = {0:1}
        n = len(nums)
        count = 0
        sum = 0

        for num in nums:
            sum+=num
            if sum-k in sumDict:
                count+= sumDict[sum-k]
            if sum in sumDict:
                sumDict[sum] += 1
            else:
                sumDict[sum] = 1
        return count


if __name__ == "__main__":
    objSol = Solution()
    nums = [1, 1, 1]
    k = 2
    print(objSol.subarraySum(nums, k))