class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if target is at mid
            if nums[mid] == target:
                return mid
            # If target is smaller, ignore right half
            elif nums[mid] > target:
                right = mid - 1
            # If target is larger, ignore left half
            else:
                left = mid + 1
                
        return -1
