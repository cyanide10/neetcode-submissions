class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        res = set()
        k = len(sorted_nums)-1


        while sorted_nums[k]>=0 and k>1:
            i = 0
            j = k-1
            while i<j:
                if sorted_nums[i]+sorted_nums[j] < -sorted_nums[k]:

                     i += 1
                elif sorted_nums[i]+sorted_nums[j] > -sorted_nums[k]:

                    j -= 1
                elif sorted_nums[i]+sorted_nums[j] == -sorted_nums[k]:

                    res.add(tuple([sorted_nums[i],sorted_nums[j],sorted_nums[k]]))
                    i += 1
                    j -= 1
                    continue
    
            k -= 1
        
        return [list(i) for i in res]