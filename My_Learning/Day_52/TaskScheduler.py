from collections import Counter

def leastInterval(tasks, n):
    
    task_count = Counter(tasks)
    
    max_frequency = max(task_count.values())
    
    max_frequency_tasks = sum(1 for count in task_count.values() if count == max_frequency)
    
    minimum_intervals = (max_frequency - 1) * (n + 1) + max_frequency_tasks
    
    return max(minimum_intervals, len(tasks))

# Test cases
tasks1 = ["A","A","A","B","B","B"]
n1 = 2
tasks2 = ["A","C","A","B","D","B"]
n2 = 1
tasks3 = ["A","A","A","B","B","B"]
n3 = 3

print(leastInterval(tasks1, n1))  # Output: 8
print(leastInterval(tasks2, n2))  # Output: 6
print(leastInterval(tasks3, n3))  # Output: 10
