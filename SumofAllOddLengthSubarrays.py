from typing import List
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sumT = 0
        for i in range( len(arr)):
            for j in range(i, len(arr),2):
                print(arr[i:j+1])
                sumT+=sum(arr[i:j+1])
        return sumT


if __name__ == "__main__":
    arr = [1,4,2,5,3]
    objSol = Solution()
    print(objSol.sumOddLengthSubarrays(arr))