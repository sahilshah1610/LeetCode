from functools import reduce
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arrayNew = []
        for x in range(n):
            arrayNew.append(start + 2*x)
        return reduce(lambda x,y:x^y, arrayNew)





if __name__ == "__main__":
    n = 1
    start = 7
    objSol = Solution()
    print(objSol.xorOperation(n, start))

