class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        sum = 0
        result = []
        if n ==1:
            result.append(0)
        else:
            for x in range(1, n):
                result.insert(x-1,x)
                sum+=x
                print(sum)
            result.append(-sum)
        return result

if __name__ == "__main__":
    n = 5
    objSol = Solution()
    print(objSol.sumZero(n))