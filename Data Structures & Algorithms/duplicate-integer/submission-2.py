class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)
        list_num = list(set_num)
        if len(list_num) == len(nums):
            return False
        else:
            return True