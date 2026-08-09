# 238. Product of Array Except Self

- 完成日期：2026-08-08
- 完成时间：23:21:36 PDT（America/Los_Angeles，UTC-07:00）
- 难度：Medium
- 题目链接：[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- 提交结果：正确

## 题目概述

给定整数数组 `nums`，返回数组 `answer`，其中 `answer[i]` 是除 `nums[i]` 之外所有元素的乘积。要求在线性时间内完成，并且不能使用除法。

## 我的题解

代码见 [`user_solution.py`](./user_solution.py)。

分别构建两个数组：

- `prefixes[i]` 保存下标 `i` 左侧全部元素的乘积。
- 反转后的 `suffixes[i]` 保存下标 `i` 右侧全部元素的乘积。
- 两者相乘得到 `answer[i]`。

复杂度：

- 时间复杂度：`O(n)`。
- 额外空间复杂度：`O(n)`，因为额外维护了 `prefixes` 和 `suffixes`。

## 标准题解

代码见 [`standard_solution.py`](./standard_solution.py)。

先把每个位置左侧的乘积写入返回数组，再从右向左维护一个滚动的后缀乘积，并直接乘到返回数组对应位置。这样无需单独保存前缀和后缀数组。

复杂度：

- 时间复杂度：`O(n)`。
- 额外空间复杂度：`O(1)`；按照题目约定，返回数组不计入额外空间。

## 错题分析与优化建议

### 正确性

本次题解没有逻辑错误。前缀与后缀的定义正确，也能正确处理数组中包含一个或多个 `0` 的情况，没有使用题目禁止的除法。

### 可以优化的地方

1. `prefixes` 和 `suffixes` 都占用 `O(n)` 空间，可以复用输出数组存放前缀积，并使用单个变量滚动维护后缀积，将额外空间降为 `O(1)`。
2. `nums[::-1]` 会创建一个完整的数组副本。可以改用倒序索引遍历，避免这部分额外内存。
3. 提交代码中保留了两个 `print` 调试语句。它们不影响结果，但会产生无关输出，并增加大输入下的运行开销，正式提交前应删除。
4. `start = start * i` 可以简写为 `start *= i`，让累乘意图更直接。

