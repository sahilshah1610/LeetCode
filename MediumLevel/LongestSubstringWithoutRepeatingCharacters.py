class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        mapping = {}
        maxLenght=start=0

        for i in range(len(s)):
            if s[i] in mapping and start <= mapping[s[i]]:
                start= mapping[s[i]] +1
            else:
                maxLenght = max(maxLenght, i-start+1)

            mapping[s[i]] = i
            #print(start, maxLenght, mapping)

        return maxLenght

if __name__ == "__main__":
    s = "abcabcbb"
    objSol = Solution()
    print(objSol.lengthOfLongestSubstring(s))