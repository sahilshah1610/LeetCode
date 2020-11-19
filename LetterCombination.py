class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits != "":
            resultInter = list()
            inputDict = {}
            inputDict['2'] = ['a', 'b', 'c']
            inputDict['3'] = ['d', 'e', 'f']
            inputDict['4'] = ['g', 'h', 'i']
            inputDict['5'] = ['j', 'k', 'l']
            inputDict['6'] = ['m', 'n', 'o']
            inputDict['7'] = ['p', 'q', 'r', 's']
            inputDict['8'] = ['t', 'u', 'v']
            inputDict['9'] = ['w', 'x', 'y', 'z']

            for x in range(len(digits)):
                resultInter.append(inputDict[digits[x]])
            combinations = []

            def combine(terms, accum):
                last = (len(terms) == 1)
                n = len(terms[0])
                for i in range(n):
                    item = accum + terms[0][i]
                    if last:
                        combinations.append(item)
                    else:
                        combine(terms[1:], item)

            combine(resultInter, '')
            return (combinations)
        return ""
if __name__ == "__main__":
    objSolution = Solution()
    digits = "23"
    print(objSolution.letterCombinations(digits))