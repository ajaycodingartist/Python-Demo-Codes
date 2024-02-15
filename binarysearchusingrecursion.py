def binary_search_recursive(arr, target, low, high):
      
    if low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid  # Target found at index mid
        elif mid_element < target:
            return binary_search_recursive(arr, target, mid + 1, high)  # Search the right half
        else:
            return binary_search_recursive(arr, target, low, mid - 1)  # Search the left half
    else:
        return -1  # Target not found in the list

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 7

result = binary_search_recursive(sorted_list, target_element, 0, len(sorted_list) - 1)

if result != -1:
    print(f"Target element {target_element} found at index {result}.")
else:
    print(f"Target element {target_element} not found in the list.")
