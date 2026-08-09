from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        suffixes = []
        start = 1
        for i in nums:
            prefixes.append(start)
            start = start * i
        start = 1
        for i in nums[::-1]:
            suffixes.append(start)
            start = start * i
        print(prefixes)
        print(suffixes)
        suffixes = suffixes[::-1]
        ans = []
        for i in range(len(nums)):
            ans.append(prefixes[i] * suffixes[i])

        return ans

