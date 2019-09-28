def partitionArray(left, right, pivot, arr=[]):

    # Move pointers closer to each other
    while left <= right:

        # Move left pointer until it reaches a value less than pivot
        while arr[left] < pivot:
            left += 1

        # Move right pointer until it reaches a value greater than pivot
        while arr[right] > pivot:
            right -= 1

        # Swap values and move indices
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Left will be partitionArray point
    return left


def sortArray(left, right, arr=[]):

    # Balance check
    if left >= right:
        return 0

    # Create pivot variable and set it equal to center
    pivot = arr[int((left + right) / 2)]
    index = partitionArray(left, right, pivot, arr)

    sortArray(left, index - 1, arr)
    sortArray(index, right, arr)


def quickSort(arr=[]):
    # Call sortArray function recursively
    return sortArray(0, len(arr) - 1, arr)


if __name__ == "__main__":
    
    arr_1 = [1, 45, 6, 1, 7, 0]
    print(arr_1)

    quickSort(arr_1)
    print(arr_1)