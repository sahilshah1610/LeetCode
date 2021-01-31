class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        if sum(gain) <= 0 and len(gain) == 1:
            return 0
        elif sum(gain) > 0 and len(gain) == 1:
            return gain[0]

        new = list()
        new.append(0)
        for each in gain:
            newValue = new[-1] + each
            new.append(newValue)
        return max(new)


if __name__ == "__main__":
    gain = [-5, 1, 5, 0, 7]
    objSol = Solution()
    print(objSol.largestAltitude(gain))