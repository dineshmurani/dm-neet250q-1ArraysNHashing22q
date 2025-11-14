"""
Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

Hint 1
A brute force solution would be to sort the given strings and check for their equality. This would be an O(nlogn + mlogm) solution. Though this solution is acceptable, can you think of a better way without sorting the given strings?

Hint 2
By the definition of the anagram, we can rearrange the characters. Does the order of characters matter in both the strings? Then what matters?

Hint 3
We can just consider maintaining the frequency of each character. We can do this by having two separate hash tables for the two strings. Then, we can check whether the frequency of each character in string s is equal to that in string t and vice versa.
"""
## Solution2 HASHMAP
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#
#         if len(s) != len(t):
#             return False
#
#         countS, countT = {}, {}
#
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#
#         return countS == countT

## Solution1 Sorting
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#
#         if len(s) != len(t):
#             return False
#
#         return sorted(s) == sorted(t)


## solution3 Hash Table USING ARRAY
class Solution:
     def isAnagram(self, s: str, t: str) -> bool:
         if len(s) != len(t):
             return False

         count = [0]  * 26
         for i in range(len(s)):
             count[ord(s[i]) - ord('a')] += 1
             count[ord(t[i]) - ord('a')] -= 1

         for val in count:
             if val != 0:
                 return False
             return True
