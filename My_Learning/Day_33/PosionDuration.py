def findPoisonedDuration(timeSeries, duration):
    if not timeSeries:
        return 0
    
    total_duration = 0
    for i in range(len(timeSeries) - 1):
        total_duration += min(timeSeries[i + 1] - timeSeries[i], duration)
    
    # Add the duration of the last attack
    total_duration += duration
    
    return total_duration

# Take user input for timeSeries array
timeSeries = list(map(int, input("Enter the time series array (separated by spaces): ").split()))

# Take user input for duration
duration = int(input("Enter the value of duration: "))

# Call the function and print the result
print("Output:", findPoisonedDuration(timeSeries, duration))
