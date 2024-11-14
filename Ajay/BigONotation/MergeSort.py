def merge_sort(nums):
    if len(nums) > 1:
        # Step 1: Find the midpoint and split the array
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        # Step 2: Recursively sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Step 3: Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in left_half
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in right_half
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1

# Example usage
nums = [12, 11, 13, 5, 6, 7]
merge_sort(nums)
print("Sorted array is:", nums)
