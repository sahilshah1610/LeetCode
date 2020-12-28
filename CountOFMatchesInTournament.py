class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while(n!=1):
            if n%2==0:
                matches += n//2
                n = n//2
            elif n%2!=0:
                matches +=(n)//2
                n = (n-1)//2 +1


        return matches


if __name__ == "__main__":
    n = 7
    objSol = Solution()
    print(objSol.numberOfMatches(n))