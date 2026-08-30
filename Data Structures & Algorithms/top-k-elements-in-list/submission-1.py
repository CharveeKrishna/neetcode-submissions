class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        result = []
        return [num for num, count in ctr.most_common(k)]

        