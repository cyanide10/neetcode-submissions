class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i,num in enumerate(nums):
            nums_dict[num] = i

        for i,num in enumerate(nums):
            difference = target - num
            if difference in nums_dict and nums_dict[difference] != i:
                return [i,nums_dict[difference]]
        return []


            
