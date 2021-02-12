class Solution:
    def arrangeCoins(self, n: int) -> int:

        count = 0
        i = 1
        while(n>=0):
            n=n-i
            count+=1
            i+=1
        return count -1

if __name__ == "__main__":
    objSol = Solution()
    n = 5
    print(objSol.arrangeCoins(n))