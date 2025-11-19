"""
Longest Common Prefix
You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Example 1:

Input: strs = ["bat","bag","bank","band"]

Output: "ba"
Example 2:

Input: strs = ["dance","dag","danger","damage"]

Output: "da"
Example 3:

Input: strs = ["neet","feet"]

Output: ""
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] is made up of lowercase English letters if it is non-empty.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

"""
test1:
Input:

strs=["bat","bag","bank","band"]
Your Output:

"ba"
Expected output:

"ba"

Test2:
Input:

strs=["dance","dag","danger","damage"]
Your Output:

"da"
Expected output:

"da"

Test3:
Input:

strs=["neet","feet"]
Your Output:

""
Expected output:

""
"""

"""
1. Horizontal Scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
"""
"""
2. Vertical Scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
"""
"""
3. Sorting
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
"""
"""
4. Trie
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

    def lcp(self, word: str, prefixLen: int) -> int:
        node = self.root
        for i in range(min(len(word), prefixLen)):
            if word[i] not in node.children:
                return i
            node = node.children[word[i]]
        return min(len(word), prefixLen)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        mini = 0
        for i in range(1, len(strs)):
            if len(strs[mini]) > len(strs[i]):
                mini = i

        trie = Trie()
        trie.insert(strs[mini])
        prefixLen = len(strs[mini])
        for i in range(len(strs)):
            prefixLen = trie.lcp(strs[i], prefixLen)
        return strs[0][:prefixLen]
"""

"""
This code finds the longest common prefix (LCP) from a list of strings. The LCP is the longest string that is at the beginning (prefix) of all strings in the list.

The strategy is to assume the first word is the LCP and then "shrink" it as you compare it against every other word in the list.

Step-by-Step Explanation
Here's a breakdown of the code, line by line.

1. Initialization

Python

prefix = strs[0]
The code starts by assuming the LCP is the entire first string in the list (strs[0]).

Example: If strs = ["flower", "flow", "flight"], then prefix is set to "flower".

2. Looping Through the List

Python

for i in range(1, len(strs)):
This for loop iterates through the rest of the strings in the list, one by one.

It starts at index 1 (the second string) because we already used the first string (at index 0) as our initial prefix.

Example: It will first process strs[1] ("flow") and then strs[2] ("flight").

3. Character-by-Character Comparison

Python

        j = 0
        while j < min(len(prefix), len(strs[i])):
            if prefix[j] != strs[i][j]:
                break
            j += 1
j = 0: A counter j is initialized to 0. This j will track the index of the characters we are comparing.

while j < min(...): This while loop compares the current prefix with the current string (strs[i]) one character at a time.

min(len(prefix), len(strs[i])): This is a safety check. It ensures the loop only runs as long as there are characters to compare in both strings. We can't compare the 5th character if one of the strings only has 4.

if prefix[j] != strs[i][j]: This is the core check. It sees if the characters at the same position j are different.

break: If the characters do not match, it means the common prefix has ended. We break out of the while loop.

j += 1: If the characters do match, we increment j to check the next pair of characters.

4. "Shrinking" the Prefix

Python

        prefix = prefix[:j]
This line runs after the while loop finishes (either by finding a mismatch or by reaching the end of a string).

At this point, j holds the length of the common prefix found between prefix and strs[i].

prefix[:j] is a Python slice that takes the prefix string from the beginning up to (but not including) index j.

This effectively "shrinks" the prefix to only the part that was common. If no common part was found (j is 0), the prefix becomes an empty string "".

5. Returning the Result

Python

    return prefix
After the for loop has finished comparing and shrinking the prefix against all the strings in the list, the variable prefix holds the final LCP.

The function returns this final prefix.

Example Walkthrough
Let's trace the code with strs = ["flower", "flow", "flight"]:

prefix = strs[0]

prefix is now "flower".

for i in range(1, len(strs)):

First loop (i = 1): Compare prefix ("flower") with strs[1] ("flow").

j=0: 'f' == 'f'. j becomes 1.

j=1: 'l' == 'l'. j becomes 2.

j=2: 'o' == 'o'. j becomes 3.

j=3: 'w' == 'w'. j becomes 4.

j=4: Loop stops because j (4) is not less than min(len("flower"), len("flow")) (which is 4).

prefix = prefix[:j]

j is 4.

prefix = prefix[:4] becomes "flow".

Second loop (i = 2): Compare prefix ("flow") with strs[2] ("flight").

j=0: 'f' == 'f'. j becomes 1.

j=1: 'l' == 'l'. j becomes 2.

j=2: 'o' != 'i'. Mismatch! The if condition is true.

break: The while loop stops.

prefix = prefix[:j]

j is 2.

prefix = prefix[:2] becomes "fl".

The for loop finishes.

return prefix

The function returns "fl".
"""