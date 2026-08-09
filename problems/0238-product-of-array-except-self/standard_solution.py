from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        for index in range(len(nums)):
            answer[index] = prefix
            prefix *= nums[index]

        suffix = 1
        for index in range(len(nums) - 1, -1, -1):
            answer[index] *= suffix
            suffix *= nums[index]

        return answer

