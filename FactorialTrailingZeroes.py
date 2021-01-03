class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        while n >= 5:
            zeroes += n//5
            n = n//5
        return zeroes


if __name__ == "__main__":
    n = 7
    objSol = Solution()
    print(objSol.trailingZeroes(n))