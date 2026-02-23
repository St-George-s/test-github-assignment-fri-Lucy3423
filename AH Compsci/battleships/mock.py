def outputduplicates (tempReadings, readingDates, middle, target):
    left = middle
    right = middle
    while left > 0 and tempReadings[left-1] == target:
        left -= 1
    
    while right < len(tempReadings) - 1 and tempReadings[right + 1] == target:
        right += 1
        
    for index in range(left, right):
        print(readingDates[index])
        print(tempReadings[index])

tempReadings = [3.1, 3.1, 3.1, 3.2, 3.3, 3.3, 3.4]
readingDates = ["21Jan", "31Feb", "7Jan", "10April", "13Oct", "4July", "5Sep"]
outputduplicates(tempReadings, readingDates, 3, 3.1)
