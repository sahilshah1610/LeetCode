class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        output = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    num1, num2, num3 = arr[i], arr[j], arr[k]
                    if abs(num1 - num2) <= a and abs(num2 - num3) <= b and abs(num3 - num1) <= c:
                        output+=1
        return output

if __name__ == "__main__":
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    objSol = Solution()
    print(objSol.countGoodTriplets(arr,a,b,c))