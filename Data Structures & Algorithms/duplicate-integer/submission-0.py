class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n]+=1
        print(freq)
        
        flag = False
        for k in freq.keys():
            print(freq[k])
            if freq[k] >= 2: 
                flag = True
        return flag 
        