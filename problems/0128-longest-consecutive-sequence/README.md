# 128. Longest Consecutive Sequence

- Completion date: 2026-08-10
- Completion time: 23:21:36 PDT (America/Los_Angeles, UTC-07:00)
- Difficulty: Medium
- Problem: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- Result: Correct

## Problem Summary

Given an unsorted array of integers, return the length of the longest consecutive elements sequence.

## Submitted Solution

See [`user_solution.py`](./user_solution.py).

The submitted solution builds a `set` for `O(1)` average membership checks, then scans the original list. A number is treated as a sequence start when `n - 1` is absent from the set. From each start, the code walks forward until the chain breaks and records the length.

Complexity:

- Time: `O(n)` average.
- Auxiliary space: `O(n)` for the hash set.

## Reference Solution

See [`standard_solution.py`](./standard_solution.py).

The reference solution keeps the same idea but iterates over the deduplicated set instead of the original list, which avoids repeating the same start check for duplicates. It also uses clearer names for the expanding right boundary.

Complexity:

- Time: `O(n)` average.
- Auxiliary space: `O(n)` for the hash set.

## Correctness Analysis and Optimization Notes

### Correctness

The submitted solution is correct. It identifies every valid sequence start by checking whether `n - 1` is missing, then expands exactly once per start. Duplicate values in the input do not break correctness because repeated start checks still lead to the same maximum length.

Test evidence:

- `[100, 4, 200, 1, 3, 2]` -> `4`
- `[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]` -> `9`
- `[]` -> `0`
- `[1, 2, 0, 1]` -> `3`

### Optimization Opportunities

1. Iterating over `set(nums)` instead of `nums` avoids repeated work when the input contains duplicates.
2. The variable name `start` is slightly misleading because it actually advances the right boundary. `end` is clearer.
3. The `else` block after `continue` is unnecessary and can be removed for readability.
4. `ans = max(ans, end - n + 1)` is the direct way to compute the inclusive length of the sequence.

## Why This Works

For any consecutive block, only the smallest number can be a start. If `n - 1` exists, then `n` belongs to a block that has already been or will be counted from its true start. This guarantees each block is expanded once, so the total work remains linear on average.

## More Complex Union-Find Variant

A valid but heavier alternative is to model each unique number as a Union-Find node:

1. Deduplicate the input and map each number to an index.
2. For every number `x`, if `x + 1` exists, union the nodes for `x` and `x + 1`.
3. Track the size of each root and return the largest set size.

This works because every consecutive chain becomes one connected component. For example, the block `1, 2, 3, 4` ends up in the same component after unions between adjacent numbers.

The tradeoff is that this approach is more verbose than the hash-set solution:

- It needs an extra `num -> id` mapping.
- It needs `parent` and `size` arrays.
- It still performs essentially linear work, but with a larger constant factor and more moving parts.

So Union-Find is a reasonable interview variation to know, but for this specific problem the hash-set start-expansion approach is usually the cleaner choice.
