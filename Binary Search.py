def binary_search(arr, target):
    """
    Perform binary search to find the target element in a sorted list.
 
    Parameters:
    - arr: The sorted list to be searched.
    - target: The element to be searched for.

    Returns:
    - If the target is found, returns the index of the target.
    - If the target is not found, returns -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid  # Target found at index mid
        elif mid_element < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return -1  # Target not found in the list

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 5

result = binary_search(sorted_list, target_element)

if result != -1:
    print(f"Target element {target_element} found at index {result}.")
else:
    print(f"Target element {target_element} not found in the list.")
