class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum,product = 0, 1
        while (n!=0):
            value = n%10
            sum += value
            product *= value
            n = n//10
        print(sum, product)
        return product-sum

if __name__ == "__main__":
    n = 234
    objSol = Solution()
    print(objSol.subtractProductAndSum(n))