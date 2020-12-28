from collections import OrderedDict
class Solution:
    def interpret(self, command: str) -> str:
        collectionDict = OrderedDict([("G","G"),("()","o"),("(al)","al")])
        for i, j in collectionDict.items():
            command = command.replace(i, j)
        return command

if __name__== "__main__":
    command = "G()()()()(al)"
    objSol = Solution()
    print(objSol.interpret(command))