class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        valueofA = int(a, 2)
        valueofB = int(b, 2)
        return ("{0:b}".format(valueofA+valueofB))


if __name__ == "__main__":
    objsolution = Solution()
    a = "1010"
    b = "1011"
    print(objsolution.addBinary(a, b))