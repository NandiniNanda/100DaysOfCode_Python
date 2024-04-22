import collections
import heapq

def topKFrequent(nums, k):
    # Step 1: Count frequencies of each element
    freq = collections.Counter(nums)
    
    # Step 2: Use a min-heap to keep track of the k most frequent elements
    min_heap = []
    
    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Step 3: Extract the k most frequent elements from the heap
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])
    
    # The result is in reverse order, so reverse it to get the correct order
    return result[::-1]

# Test cases
print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1,2]
print(topKFrequent([1], 1))             # Output: [1]
