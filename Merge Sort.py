def mergeSort(arr):
    
    # If list isn't empty, continue
    if len(arr) > 1:
    
        # Get mid point
        mid = len(arr) // 2
        
        # Split list into 2 halves
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]
        
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        
        # Create 3 index variables for all lists
        leftIdx = 0
        rightIdx = 0
        sortIdx = 0
        
        # Iterate leftHalf and rightHalf
        while leftIdx < len(leftHalf) and rightIdx < len(rightHalf):
            
            # Compare values
            if leftHalf[leftIdx] <= rightHalf[rightIdx]:
                
                # Update element in arr
                arr[sortIdx] = leftHalf[leftIdx]
                
                # Update index
                leftIdx += 1
                
            else:
                
                # Update element in arr
                arr[sortIdx] = rightHalf[rightIdx]
                
                # Update index
                rightIdx += 1
                
            # Update index of sortedList
            sortIdx += 1
            
        # Add remaining elements from leftHalf to arr
        while leftIdx < len(leftHalf):
            arr[sortIdx] = leftHalf[leftIdx]
            leftIdx += 1
            sortIdx += 1
            
        # Add remaining elements from rightHalf to arr
        while rightIdx < len(rightHalf):
            arr[sortIdx] = rightHalf[rightIdx]
            rightIdx += 1
            sortIdx += 1
    
arr = [12, 89, 12, 43, 0, 3, 7, 6]
mergeSort(arr)
print(arr)
