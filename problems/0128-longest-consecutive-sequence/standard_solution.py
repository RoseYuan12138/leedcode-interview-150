from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        for n in num_set:
            if n - 1 in num_set:
                continue

            end = n
            while end + 1 in num_set:
                end += 1

            best = max(best, end - n + 1)

        return best
