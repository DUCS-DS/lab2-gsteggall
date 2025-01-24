
def monotonic(lst):
   #If the list is empty, it is monotonic.
    if len(lst) == 0:
        return True
    
    #Checking if the list is increasing (ascending)
    is_increasing = True 
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            is_increasing = False
            break
    
    #Checking if the list is Decreasing.
    is_decreasing = True
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            is_decreasing = False
            break

    #Return True if the list is increasing or decreasing. 
    return is_increasing or is_decreasing

#Test Examples
print(monotonic([1,2,3,4,5]))
print(monotonic([6,5,4,3,2]))
print(monotonic([1,3,4,2,4]))
print(monotonic([]))
print(monotonic([1,1,1,1,1]))
print(monotonic([1]))

