from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = "".join([x for y, x in sorted(zip(indices, s))])
        return output

if __name__ == "__main__":
    s = "aiohn"
    indices = [3,1,4,2,0]
    objSol = Solution()
    print(objSol.restoreString(s, indices))