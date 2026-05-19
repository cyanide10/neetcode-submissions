class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        set_nums = set(nums)

        for num in set_nums:
            if (num-1) not in set_nums:
                length = 1
                while (num + length) in set_nums:
                    length += 1
                longest_seq = max(length,longest_seq)
        
        return longest_seq
                
