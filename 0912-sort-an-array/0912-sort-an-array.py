class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        def mergeSort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            left_sorted = mergeSort(left)
            right_sorted = mergeSort(right)

            return merge(left_sorted, right_sorted)

        def merge(left: List[int], right: List[int]) -> List[int]:
            sorted_array = []
            left_index, right_index = 0, 0

            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    sorted_array.append(left[left_index])
                    left_index += 1
                else:
                    sorted_array.append(right[right_index])
                    right_index += 1

            sorted_array.extend(left[left_index:])
            sorted_array.extend(right[right_index:])

            return sorted_array

        return mergeSort(nums)