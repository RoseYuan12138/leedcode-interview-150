from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the start
        ans = 0
        hashset = set(nums)
        for n in nums:
            if n - 1 in hashset:
                continue
            else:
                start = n + 1
                while start in hashset:
                    start += 1
                ans = max(ans, start - n)
        return ans
