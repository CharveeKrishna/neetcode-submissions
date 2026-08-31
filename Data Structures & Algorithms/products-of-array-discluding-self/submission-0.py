class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodres = 1
        zero_cnt =0
        for n in nums:
            if n!=0:
                prodres*= n
            else: zero_cnt +=1

        if zero_cnt > 1: 
            return [0]*len(nums)

 

        output = [0]*len(nums)
        for i, c in enumerate(nums):
            if zero_cnt : output[i]=0 if c else prodres
            else: 
                output[i] = prodres // c
        return output

        