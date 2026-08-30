class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 +count.get(num,0)

        res = sorted(count.items(), key = lambda x:x[1])

        ans = []
        while k > 0  :
            ans.append(res.pop()[0])
            k-=1
        return ans






        