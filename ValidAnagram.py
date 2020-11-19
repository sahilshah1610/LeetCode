class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

if __name__ == "__main__":
    objSolution = Solution()
    s = "rat"
    t = "car"
    print(objSolution.isAnagram(s,t))