from typing import List
class Solution:
    def average(self, salary: List[int]) -> float:
        del salary[salary.index(min(salary))]
        del salary[salary.index(max(salary))]
        return sum(salary)/len(salary)


if __name__ == "__main__":
    objSol = Solution()
    salary = [4000,3000,1000,2000]
    print(objSol.average(salary))