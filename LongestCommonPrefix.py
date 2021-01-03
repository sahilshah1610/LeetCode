from typing import List
from itertools import combinations
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPreffix = ""
        if len(strs)==0: return commonPreffix
        for x in range(len(min(strs))):
            charC = strs[0][x]
            if all(a[x]==charC for a in strs):
                commonPreffix+=charC
            else:
                break
        return commonPreffix
        

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    objSol = Solution()
    print(objSol.longestCommonPrefix(strs))