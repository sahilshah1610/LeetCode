from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for x in range(len(words)):
            if len(set(words[x]).difference(set(allowed))) == 0:
                count +=1
        return count

if __name__ == "__main__":
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    objSol = Solution()
    print(objSol.countConsistentStrings(allowed, words))
