from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(arr)for arr in accounts])


if __name__ == "__main__":
    arr = [[1,5],[7,3],[3,5]]
    objSol = Solution()
    print(objSol.maximumWealth(arr))