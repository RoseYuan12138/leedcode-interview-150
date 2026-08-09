# 238. Product of Array Except Self

- Completion date: 2026-08-08
- Completion time: 23:21:36 PDT (America/Los_Angeles, UTC-07:00)
- Difficulty: Medium
- Problem: [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- Result: Correct

## Problem Summary

Given an integer array `nums`, return an array `answer` where `answer[i]` is the product of every element except `nums[i]`. The solution must run in linear time without using division.

## Submitted Solution

See [`user_solution.py`](./user_solution.py).

The submitted solution builds two arrays:

- `prefixes[i]` stores the product of all elements to the left of index `i`.
- After reversal, `suffixes[i]` stores the product of all elements to the right of index `i`.
- Multiplying these values produces `answer[i]`.

Complexity:

- Time: `O(n)`.
- Auxiliary space: `O(n)` because `prefixes` and `suffixes` are stored separately.

## Reference Solution

See [`standard_solution.py`](./standard_solution.py).

First, write the product of all preceding elements into each position of the output array. Then traverse from right to left, maintaining a rolling suffix product and multiplying it directly into the corresponding output position. This avoids separate prefix and suffix arrays.

Complexity:

- Time: `O(n)`.
- Auxiliary space: `O(1)` when the output array is excluded, as specified by the problem.

## Correctness Analysis and Optimization Notes

### Correctness

The submitted solution has no logical errors. Its prefix and suffix definitions are correct, it handles arrays containing one or more zeroes, and it does not use division.

### Optimization Opportunities

1. Both `prefixes` and `suffixes` use `O(n)` space. The output array can store prefix products while a single variable tracks the rolling suffix product, reducing auxiliary space to `O(1)`.
2. `nums[::-1]` creates a full copy of the input. Iterating over indices in reverse avoids that additional allocation.
3. The two debugging `print` statements do not affect correctness, but they produce unrelated output and add overhead for large inputs. They should be removed before submission.
4. `start = start * i` can be written as `start *= i` to express the accumulation more directly.
