import bisect

def findRightInterval(intervals):
    n = len(intervals)
    # Sort the intervals based on their start points
    sorted_intervals = sorted((interval[0], i) for i, interval in enumerate(intervals))
    result = [-1] * n
    
    for i, interval in enumerate(intervals):
        end_point = interval[1]
        # Perform binary search to find the right interval
        index = bisect.bisect_left(sorted_intervals, (end_point,))
        if index < n:
            result[i] = sorted_intervals[index][1]
    
    return result

# Test cases
intervals1 = [[1,2]]
intervals2 = [[3,4],[2,3],[1,2]]
intervals3 = [[1,4],[2,3],[3,4]]

print(findRightInterval(intervals1)) # Output: [-1]
print(findRightInterval(intervals2)) # Output: [-1, 0, 1]
print(findRightInterval(intervals3)) # Output: [-1, 2, -1]
