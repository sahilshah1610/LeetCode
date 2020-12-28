class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        fb = flowerbed
        fb = [0] + fb + [0]
        i = 1
        while i < len(fb) - 1:
            if fb[i] == 0 and fb[i + 1] == 0 and fb[i - 1] == 0:
                n -= 1
                i += 2

            else:
                i += 1

            if n == 0:
                return True

        return False
        # for x in range(len(flowerbed)-2):
        #     if 1 not in flowerbed[x:x+3]:
        #         del flowerbed[x+1]
        #         flowerbed.insert(x+1, 1)
        #         n = n-1
        # return (n==0)


if __name__ == "__main__":
    objSol = Solution()
    flowerbed = [1,0,0,0,1]
    n = 1
    print(objSol.canPlaceFlowers(flowerbed, n))