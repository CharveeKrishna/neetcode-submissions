from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ctr = Counter(nums)
        print(ctr)
        for val in ctr.values():
            if val > 1: 
                return True
        return False
        