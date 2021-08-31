values = [47, 95, 88, 73, 88, 84];

# Count
def getCount(values):
    count = 0
    for element in values:
        count += 1
    return count

print("Number of elements in the list: ", getCount(values))

#Sum
total = 0;
for i in values:
     total = total + i

print("Sum:",total);

#Mean
def getMean(values):
    sum = 0
    for element in values:
        sum = sum + element
    avg = sum / len(values)
    return avg

print("Number of elements in the list: ", getMean(values))


#Median
def median(L):
    L.sort()
    if len(L)%2 != 0:
        median = L[int(len(L)/2)]
    else:
        median = L[(int(len(L)/2)) - 1] +  L[int(len(L)/2)]
        median = median/2
    return median
print("Number of elements in the list: ", median(values))

#Mode
from collections import Counter
  
# list of elements to calculate mode
mode = max(values, key = values.count)
print(mode)
