"""
Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.


Recommended Time & Space Complexity

Hint 1
A naive solution would be to count the frequency of each number and then sort the array based on each element’s frequency. After that, we would select the top k frequent elements. This would be an O(nlogn) solution. Though this solution is acceptable, can you think of a better way?


Hint 2
Can you think of an algorithm which involves grouping numbers based on their frequency?


Hint 3
Use the bucket sort algorithm to create n buckets, grouping numbers based on their frequencies from 1 to n. Then, pick the top k numbers from the buckets, starting from n down to 1.

Video Explanation


View on Youtube

1. Sorting
Intuition
To find the k most frequent elements, we first need to know how often each number appears.
Once we count the frequencies, we can sort the unique numbers based on how many times they occur.
After sorting, the numbers with the highest frequencies will naturally appear at the end of the list.
By taking the last k entries, we get the k most frequent elements.

This approach is easy to reason about:
count the frequencies → sort by frequency → take the top k.

Algorithm
Create a hash map to store the frequency of each number.
Build a list of [frequency, number] pairs from the map.
Sort this list in ascending order based on frequency.
Create an empty result list.
Repeatedly pop from the end of the sorted list (highest frequency) and append the number to the result.
Stop when the result contains k elements.
Return the result list.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
Time & Space Complexity
Time complexity:
O
(
n
log
⁡
n
)
O(nlogn)
Space complexity:
O
(
n
)
O(n)
2. Min-Heap
Intuition
After counting how often each number appears, we want to efficiently keep track of only the k most frequent elements.
A min-heap is perfect for this because it always keeps the smallest element at the top.
By pushing (frequency, value) pairs into the heap and removing the smallest whenever the heap grows beyond size k, we ensure that the heap always contains the top k most frequent elements.
In the end, the heap holds exactly the k values with the highest frequencies.

Algorithm
Build a frequency map that counts how many times each number appears.
Create an empty min-heap.
For each number in the frequency map:
Push (frequency, number) into the heap.
If the heap size becomes greater than k, pop once to remove the smallest frequency.
After processing all numbers, the heap contains the k most frequent elements.
Pop all elements from the heap and collect their numbers into the result list.
Return the result.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
Time & Space Complexity
Time complexity:
O
(
n
log
⁡
k
)
O(nlogk)
Space complexity:
O
(
n
+
k
)
O(n+k)
Where
n
n is the length of the array and
k
k is the number of top frequent elements.
3. Bucket Sort
Intuition
Each number in the array appears a certain number of times, and the maximum possible frequency is the length of the array.
We can use this idea by creating a list where the index represents a frequency, and at each index we store all numbers that appear exactly that many times.

For example:

All numbers that appear 1 time go into group freq[1].
All numbers that appear 2 times go into group freq[2].
And so on.
After we build these groups, we look from the highest possible frequency down to the lowest and collect numbers from these groups until we have k of them.
This way, we directly jump to the most frequent numbers without sorting all the elements by frequency.

Algorithm
Build a frequency map that counts how many times each number appears.
Create a list of groups freq, where freq[i] will store all numbers that appear exactly i times.
For each number and its frequency in the map, add the number to freq[frequency].
Initialize an empty result list.
Loop from the largest possible frequency down to 1:
For each number in freq[i], add it to the result list.
Once the result contains k numbers, return it.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

"""
Below is a clear, detailed, line-by-line explanation of the Python code.
This is a common solution to the Top K Frequent Elements problem (LeetCode 347).

✅ High-Level Goal

Given a list of integers nums and an integer k, return the k most frequent elements.

This solution uses:

A hash map (count) to count occurrences

A bucket sort list (freq) to group numbers by frequency

Then iterates buckets from high → low frequency to collect the top k

✅ Code Explained
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

1. count = {}

Creates an empty dictionary to store frequency of each number:

number → its count


Example:
for nums = [1,1,2,3,3,3]
count becomes: {1: 2, 2: 1, 3: 3}

2. freq = [[] for i in range(len(nums) + 1)]

Creates a list of empty lists ("buckets").

Why len(nums) + 1?

A number can appear at most len(nums) times.

Index = frequency.

Example for 6 numbers → need buckets 0..6 → 7 lists.

Structure:

freq[0] = []
freq[1] = numbers that appear 1 time
freq[2] = numbers that appear 2 times
…
freq[6] = numbers that appear 6 times

Count frequencies
for n in nums:
    count[n] = 1 + count.get(n, 0)


Loops through each number in nums:

count.get(n, 0) returns the current count, or 0 if not present.

Adds 1 to update the frequency.

Group numbers by their frequency
for n, c in count.items():
    freq[c].append(n)


For each number n and its count c:

Put n into the bucket that corresponds to frequency c.

Example:
If counts are {1:2, 2:1, 3:3}

freq[1] = [2]
freq[2] = [1]
freq[3] = [3]

Collect the top k frequent numbers
res = []
for i in range(len(freq) - 1, 0, -1):
    for n in freq[i]:
        res.append(n)
        if len(res) == k:
            return res

What this does:

Start from the highest frequency (len(freq)-1)

Move downwards (reverse bucket order)

At each frequency bucket, take all numbers inside it

Add them to result list

Stop immediately once we have collected k numbers

This is very efficient:
No need to sort anything → O(n) time.

🚀 Example Walkthrough

Input:

nums = [1,1,1,2,2,3], k = 2

Step 1: count frequencies
count = {1:3, 2:2, 3:1}

Step 2: build buckets
freq = [
 [],      # 0 occurrences
 [3],     # 1 occurrence
 [2],     # 2 occurrences
 [1],     # 3 occurrences
 [], [], [], # extra buckets depending on nums length
]

Step 3: collect from highest freq → lowest

Start from freq[6] → empty

...

freq[3] = [1] → res = [1]

freq[2] = [2] → res = [1, 2] → return this

Output:

[1, 2]

⭐ Why This Solution Is Good
Feature	Benefit
Uses bucket sort	Avoids slow sorting → O(n) time
No extra complex data structures	Simple and efficient
Early stopping	Stops once top k found
✔ Final Explained Summary

This code:

Counts how many times each number appears

Creates frequency buckets

Places each number into the bucket corresponding to its frequency

Reads buckets from highest frequency to lowest

Returns the first k numbers encountered

So the algorithm is efficient and elegant for the "top K frequent" problem.

If you'd like, I can also provide:

✅ A simplified version
✅ A version using collections.Counter
✅ Time–space complexity analysis
✅ Visualization diagrams

Just tell me!
"""