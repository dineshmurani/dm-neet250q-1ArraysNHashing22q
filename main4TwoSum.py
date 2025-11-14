"""
Two Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input:
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000


Recommended Time & Space Complexity

Hint 1
A brute force solution would be to check every pair of numbers in the array. This would be an O(n^2) solution. Can you think of a better way? Maybe in terms of mathematical equation?


Hint 2
Given, We need to find indices i and j such that i != j and nums[i] + nums[j] == target. Can you rearrange the equation and try to fix any index to iterate on?


Hint 3
we can iterate through nums with index i. Let difference = target - nums[i] and check if difference exists in the hash map as we iterate through the array, else store the current element in the hashmap with its index and continue. We use a hashmap for O(1) lookups.

Youtube video:
https://neetcode.io/problems/two-integer-sum?list=neetcode250


1. Brute Force
Intuition
We can check every pair of different elements in the array and return the first pair that sums up to the target. This is the most intuitive approach but it's not the most efficient.

Algorithm
Iterate through the array with two nested loops to check every pair of different elements.
If the sum of the pair equals the target, return the indices of the pair.
If no such pair is found, return an empty array.
There is guaranteed to be exactly one solution, so we will never return an empty array.
"""
# # 1. Brute Force
# class Solution:
#     def twoSum(self, nums: List[int], target: list[int]) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []
#
# # Test1 Input:
# # nums=[3,4,5,6]
# # target=7
# # Your Output:
# # [0,1]
# # Expected output:
# # [0,1]
# # Test2
# # Input:
# # nums=[4,5,6]
# # target=10
# # Your Output:
# # [0,2]
# # Expected output:
# # [0,2]

"""
2. Sorting
Intuition
We can sort the array and use two pointers to find the two numbers that sum up to the target. This is more efficient than the brute force approach. This approach is similar to the one used in Two Sum II.

Algorithm
Create a copy of the array and sort it in ascending order.
Initialize two pointers, one at the beginning and one at the end of the array.
Iterate through the array with the two pointers and check if the sum of the two numbers is equal to the target.
If the sum is equal to the target, return the indices of the two numbers.
If the sum is less than the target, move the left pointer to the right, which will increase the sum.
If the sum is greater than the target, move the right pointer to the left, which will decrease the sum.
There is guaranteed to be exactly one solution, so we will never return an empty array.
"""
# class Solution:
#     def twoSum(self, nums: List[int], target: list[int]) -> list[int]:
#         A = []
#         for i, num in enumerate(nums):
#             A.append([num, i])
#
#         A.sort()
#         i, j = 0, len(nums) - 1
#         while i < j:
#             cur = A[i][0] + A[j][0]
#             if cur == target:
#                 return [min(A[i][1],A[j][1]),
#                         max(A[i][1], A[j][1])]
#             elif cur < target:
#                 i += 1
#             else:
#                 j -= 1
#         return []


"""
3. Hash Map (Two Pass)
Intuition
We can use a hash map to store the value and index of each element in the array. Then, we can iterate through the array and check if the complement of the current element exists in the hash map. The complement must be at a different index, because we can't use the same element twice.

By using a hashmap, we can achieve a time complexity of 
O
(
n
)
O(n) because the insertion and lookup time of a hashmap is 
O
(
1
)
O(1).

Algorithm
Create a hash map to store the value and index of each element in the array.
Iterate through the array and compute the complement of the current element, which is target - nums[i].
Check if the complement exists in the hash map.
If it does, return the indices of the current element and its complement.
If no such pair is found, return an empty array.
"""
class Solution:
    def twoSum(self, nums: List[int], target: list[int]) -> list[int]:
        indices = {} # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
