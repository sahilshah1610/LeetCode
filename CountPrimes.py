import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        count = 0
        primes = [False for _ in range(n+1)]

        for x in range(2,n):
            if primes[x]==False:
                count+=1
                j = 2
                while j*x<n:
                    primes[j*x] = True
                    j+=1
        return count



if __name__ == "__main__":
    n = 10
    objSol = Solution()
    print(objSol.countPrimes(n))