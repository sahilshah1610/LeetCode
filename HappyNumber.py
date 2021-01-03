class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        cycleSet = set()
        while sum != 1 :
            sum = 0
            strNumList = list(str(n))
            for x in strNumList:
                sum += int(x)**2
            if sum in cycleSet:
                return False
            cycleSet.add(sum)
            if sum == 1:
                return True
            n = sum
        return False

if __name__ == "__main__":
    n = 1
    objSol = Solution()
    print(objSol.isHappy(n))