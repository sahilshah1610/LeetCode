class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        splitSentence = sentence.split()
        for index, each in enumerate(splitSentence):
            if each.startswith(searchWord):
                return index+1
        return -1


if __name__ == "__main__":
    sentence = "i love eating burger"
    searchWord = "burg"
    objSol = Solution()
    print(objSol.isPrefixOfWord(sentence, searchWord))