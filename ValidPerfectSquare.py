class Solution(object):


    def validSqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return (x ** (1 / 2)).is_integer()


if __name__ == "__main__":
    objSolution = Solution()
    print(objSolution.validSqrt(15))