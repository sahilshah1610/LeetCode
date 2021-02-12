class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        i = 1
        while(i<len(intervals)):
            if intervals[i][0] <= intervals[i-1][1]:
                starting = min(intervals[i-1][0], intervals[i][0])
                ending = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
                intervals[i-1] = [starting, ending]
            else:
                i+=1
        return intervals

#intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
objSol = Solution()
print(objSol.merge(intervals))