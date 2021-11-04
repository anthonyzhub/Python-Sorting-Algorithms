"""
Time complexity is O(n log n) in the best-case scenario, while worst-case scenario is O(n^2). A worst-case scenario is when the list is sorted in descending order,
so it will take more time to sort the list in ascending order.

Space complexity is O(n). In both measurements, "n" represents the number of nodes inside the list.
"""

def splitList(arr, pivot, leftPtr, rightPtr):
    
    # Iterate list
    while leftPtr <= rightPtr:
        
        # Move leftPtr until it reaches an element greater than pivot
        while arr[leftPtr] < pivot:
            leftPtr += 1
            
        # Move rightPtr until it reaches an element less than pivot
        while arr[rightPtr] > pivot:
            rightPtr -= 1
            
        # When both inner while-loops stop, swap values
        if leftPtr <= rightPtr:
            
            # Swap values
            arr[leftPtr], arr[rightPtr] = arr[rightPtr], arr[leftPtr]
            
            # Update indexes
            leftPtr += 1
            rightPtr -= 1
            
    # Return leftPtr for further use
    return leftPtr

def sortList(arr, leftPtr, rightPtr):
    
    # If pointers overlap, exit function
    if leftPtr >= rightPtr:
        return
    
    # Create a pivot
    midIdx = (leftPtr + rightPtr) // 2
    pivot = arr[midIdx]

    # Get index of where to split list
    idx = splitList(arr, pivot, leftPtr, rightPtr)
    
    # Make a recursive call to shorten list
    sortList(arr, leftPtr, idx - 1)
    sortList(arr, idx, rightPtr)

def quickSort(arr):
    sortList(arr, 0, len(arr) - 1)
    
arr = [12, 89, 12, 43, 0, 3, 7, 6]
quickSort(arr)
print(arr)
