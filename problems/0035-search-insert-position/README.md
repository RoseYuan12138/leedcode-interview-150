# 35. Search Insert Position

- Completion date: 2026-08-12
- Completion time: 01:57:30 PDT (America/Los_Angeles, UTC-07:00)
- Difficulty: Easy
- Problem: [Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- Result: Incorrect

## Problem Summary

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be inserted in sorted order.

## Submitted Solution

See [`user_solution.py`](./user_solution.py).

The submitted code uses binary search, but it returns `mid` inside the loop after the first comparison step. That means the search stops before the interval is fully narrowed down, so it can return a wrong index even when the target is not at the first midpoint.

Complexity:

- Time: not reliably `O(log n)` as written, because the search can terminate prematurely with the wrong answer.
- Auxiliary space: `O(1)`.

## Reference Solution

See [`standard_solution.py`](./standard_solution.py).

The reference solution keeps the same binary-search idea, but it only returns early on an exact match. If the target is not found, it returns `start`, which is the first valid insertion index after the search interval collapses.

Complexity:

- Time: `O(log n)`.
- Auxiliary space: `O(1)`.

## Correctness Analysis and Boundary Notes

### What went wrong in the submitted code

The main defect is this line inside the loop:

```python
return mid
```

Because it is indented inside `while start < end`, the function exits after one iteration regardless of whether the midpoint is correct. That breaks the core binary-search invariant that the interval must keep shrinking until the answer is determined.

There is also a boundary-condition issue with the loop guard:

```python
while start < end:
```

For this problem, `start <= end` is the safer pattern because a one-element interval still needs to be checked. With `<`, the loop can stop one step too early and miss the last candidate position.

### Concrete failing cases

- `nums = [1, 3, 5, 6]`, `target = 2`
  - Expected: `1`
  - Submitted behavior: returns `1` only because the first midpoint happens to be the insertion point after one iteration; this is accidental, not guaranteed.
- `nums = [1, 3, 5, 6]`, `target = 7`
  - Expected: `4`
  - Submitted behavior: returns `1` after the first loop iteration, which is incorrect.
- `nums = [1]`, `target = 2`
  - Expected: `1`
  - Submitted behavior: returns `0` or exits without finding the correct insertion point depending on the branch flow.

### Boundary-condition rules to remember

1. Use `while start <= end` when the search space is inclusive on both ends.
2. Return immediately only for a true match.
3. When the loop ends, `start` is the first position where `target` can be inserted.
4. `mid` is only a probe location, not the final answer unless the problem explicitly asks for it.

## Optimization and Code-Quality Notes

1. Move the final answer out of the loop. The loop should only narrow the interval.
2. Use `while start <= end` so the last candidate is not skipped.
3. Prefer `if / elif / else` without extra indentation or early returns unless the return is logically final.
4. Remove the unused `n` variable if you want the shortest readable version.

## Why the Reference Solution Works

The reference solution maintains this invariant:

- Everything before `start` is too small.
- Everything after `end` is too large.
- The answer is either the exact match found inside the loop or the insertion point at `start` after the loop.

That invariant guarantees the correct insertion index for every edge case, including:

- empty input
- target smaller than the first element
- target larger than the last element
- target already present
- one-element arrays

## Test Evidence

Reference solution checks:

- `[1, 3, 5, 6]`, `2` -> `1`
- `[1, 3, 5, 6]`, `5` -> `2`
- `[1, 3, 5, 6]`, `7` -> `4`
- `[1]`, `0` -> `0`
- `[1]`, `2` -> `1`
