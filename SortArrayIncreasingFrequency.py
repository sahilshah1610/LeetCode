from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        new = []
        counts = [(x, nums.count(x))for x in set(nums)]
        counts = sorted(counts, key=lambda i:(i[1], -i[0]))
        for x in counts:
            new +=x[1]*[x[0]]

        return new


if __name__ == "__main__":
    nums = [-1,1,-6,4,5,-6,1,4,1]
    objSol = Solution()
    print(objSol.frequencySort(nums))