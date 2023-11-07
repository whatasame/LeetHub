class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        
        for interval in intervals:
            # after interval -> add interval
            if interval[1] < newInterval[0]:
                answer.append(interval)

            # before interval -> add newInterval
            elif interval[0] > newInterval[1]:
                answer.append(newInterval)
                newInterval = interval # to add remains

            # merge
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        answer.append(newInterval)

        return answer