class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return sum(nums)
        
        max_sum = 0
        current_sum = 0
        freq = defaultdict(int)
        
        # Initialize the window
        for i in range(k):
            current_sum += nums[i]
            freq[nums[i]] += 1
        
        # Check the first window
        if len(freq) == k:
            max_sum = current_sum
        
        # Slide the window
        for i in range(k, len(nums)):
            # Remove the leftmost element
            left_elem = nums[i - k]
            current_sum -= left_elem
            freq[left_elem] -= 1
            if freq[left_elem] == 0:
                del freq[left_elem]
            
            # Add the new element
            right_elem = nums[i]
            current_sum += right_elem
            freq[right_elem] += 1
            
            # If the current window has exactly k unique elements, update max_sum
            if len(freq) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum