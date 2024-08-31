class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_interval = [intervals[0]]

        for start, end in intervals[1:]:
            if merged_interval[-1][1] < start:
                merged_interval.append([start,end])
            else:
                merged_interval[-1][1] = max(merged_interval[-1][1],end)
        
        return merged_interval