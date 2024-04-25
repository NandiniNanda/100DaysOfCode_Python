def reconstructQueue(people):
    # Sort people array based on height (hi) descending and ki ascending
    people.sort(key=lambda x: (-x[0], x[1]))
    
    # Initialize the result list
    result = []
    
    # Insert each person into the result list at the specified index (ki)
    for person in people:
        result.insert(person[1], person)
    
    return result

# Test the reconstructQueue function with example inputs
people1 = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(people1))  # Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

people2 = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(reconstructQueue(people2))  # Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
