class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0)+1
        
        freq = sorted(counter.items(), key = lambda x:x[1])

        res = []
        while len(res)<k:
            res.append(freq.pop()[0])
        return res 
        