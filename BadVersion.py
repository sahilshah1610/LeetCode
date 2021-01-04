# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        while(start<end):
            mid = start +(start-end)//2
            if isBadVersion(mid):
                temp = mid
                end = mid-1
            else:
                start = mid+1

        return temp



if __name__ == "__main__":
    n = 5
    objSol = Solution()
    print(objSol.firstBadVersion(n))