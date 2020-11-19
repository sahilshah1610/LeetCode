class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #return int(x**(1/2.0))

        # Solution to 367
        print(type(x))
        
        return (x**(1/2)).is_integer()


if __name__ == "__main__":
    objSolution = Solution()
    print(objSolution.mySqrt(16))