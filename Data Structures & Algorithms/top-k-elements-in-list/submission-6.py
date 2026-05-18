class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        res = []
        for num in nums:
            freq_map.setdefault(num,0)
            freq_map[num] += 1
        freq_map_sorted = dict(sorted(freq_map.items(),key = lambda item : item[1], reverse = True))
        for i,num in enumerate(freq_map_sorted):
            if i < k:
                res.append(num)
        return res