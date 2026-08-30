class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_Set = set()
        for num in nums:
            if num in seen_Set: 
                return True
            seen_Set.add(num)
        return False 
        