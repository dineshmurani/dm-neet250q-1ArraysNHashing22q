"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.


Recommended Time & Space Complexity

Hint 1
A naive solution would be to use a non-ascii character as a delimiter. Can you think of a better way?


Hint 2
Try to encode and decode the strings using a smart approach based on the lengths of each string. How can you differentiate between the lengths and any numbers that might be present in the strings?


Hint 3
We can use an encoding approach where we start with a number representing the length of the string, followed by a separator character (let's use # for simplicity), and then the string itself. To decode, we read the number until we reach a #, then use that number to read the specified number of characters as the string.

SOLUTION:
1. Encoding & Decoding
Intuition
To encode a list of strings into a single string, we need a way to store each string so that we can later separate them correctly during decoding.
A simple and reliable strategy is to record the length of each string first, followed by a special separator, and then append all the strings together.
During decoding, we can read the recorded lengths to know exactly how many characters to extract for each original string.
This avoids any issues with special characters, commas, or symbols inside the strings because the lengths tell us precisely where each string starts and ends.

Algorithm
Encoding
If the input list is empty, return an empty string.
Create an empty list to store the sizes of each string.
For each string, append its length to the sizes list.
Build a single string by:
Writing all sizes separated by commas.
Adding a '#' to mark the end of the size section.
Appending all the actual strings in order.
Return the final encoded string.
Decoding
If the encoded string is empty, return an empty list.
Read characters from the start until reaching '#' to extract all recorded sizes:
Parse each size by reading until a comma.
After the '#', extract substrings according to the sizes list:
For each size, read that many characters and append the substring to the result.
Return the list of decoded strings.

class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
Time & Space Complexity
Time complexity:
O
(
m
)
O(m) for each
e
n
c
o
d
e
(
)
encode() and
d
e
c
o
d
e
(
)
decode() function calls.
Space complexity:
O
(
m
+
n
)
O(m+n) for each
e
n
c
o
d
e
(
)
encode() and
d
e
c
o
d
e
(
)
decode() function calls.
Where
m
m is the sum of lengths of all the strings and
n
n is the number of strings.
2. Encoding & Decoding (Optimal)
Intuition
Instead of storing all string lengths first and then appending the strings, we can directly attach each string to its length.
For every string, we write length#string.
The # character acts as a clear boundary between the length and the actual content, and using the length ensures we know exactly how many characters to read—no matter what characters appear in the string itself.
During decoding, we simply read characters until we reach # to find the length, then extract exactly that many characters as the string.
This approach is both simpler and more efficient because it avoids building separate sections for lengths and content.

Algorithm
Encoding
Initialize an empty result string.
For each string in the list:
Compute its length.
Append "length#string" to the result.
Return the final encoded string.
Decoding
Initialize an empty list for the decoded strings and a pointer i = 0.
While i is within the bounds of the encoded string:
Move a pointer j forward until it finds '#' — this segment represents the length.
Convert the substring s[i:j] into an integer length.
Move i to the character right after '#'.
Extract the next length characters — this is the original string.
Append the extracted string to the result list.
Move i forward by length to continue decoding the next segment.
Return the list of decoded strings.

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res

"""
this is the classic encode/decode string list solution (LeetCode 271). I’ll walk through it step-by-step, explain why it works, show examples (including tricky cases), and finish with runtime/space complexity and possible improvements.

What the code does (high level)

encode turns a list of strings strs into one single string so it can be stored/transmitted.

decode reverses that process and recovers the original list of strings from the single encoded string.

The trick: each string is stored as "<length>#<string>". The numeric length tells the decoder exactly how many characters to read next, so the content can contain # or any character without ambiguity.

The code (annotated)
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


Line-by-line:

res = ""
Create an empty string that will accumulate the encoded result.

for s in strs:
Loop over every string s in the input list.

res += str(len(s)) + "#" + s

len(s) computes how many characters are in s.

str(len(s)) converts that number to text.

"#" is used as a separator between the length and the string content. Using # is safe because the length prefix tells the decoder exactly how many characters to read — the presence of # inside s doesn't break anything.

Concatenate these three pieces and append to the running result.

return res
Return the single encoded string built by joining all "<length>#<string>" blocks.

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


Line-by-line:

res, i = [], 0

res will collect the decoded strings.

i is the current index in the encoded string s (cursor pointer).

while i < len(s):
Loop until the cursor reaches the end of the encoded string.

j = i
Start another pointer j at the same position as i. j will find the # separator.

while s[j] != "#": j += 1
Move j forward until it reaches the #. The substring s[i:j] is the decimal digits of the length we stored.

Important: this assumes a well-formed encoding so # will be found before the string ends.

length = int(s[i:j])
Convert the digit substring into an integer — that is the number of characters to read next.

res.append(s[j + 1 : j + 1 + length])
Slice the next length characters after the # and append that substring to the result list.

i = j + 1 + length
Advance i to the position after the characters we just read; loop continues to decode the next item.

return res
After the loop finishes, return the list of decoded strings.

Example

Input:

strs = ["hello", "world", "", "a#b"]


Encoding steps:

"hello" → "5#hello"

"world" → "5#world"

"" (empty string) → "0#"

"a#b" → "3#a#b" (length is 3, content contains # but that's fine)

Final encoded string:

"5#hello5#world0#3#a#b"


Decoding:

Start at i = 0, read digits until # → 5, read next 5 chars → "hello".

Move to next, read 5 → "world".

Next 0 → empty string "".

Next 3 → read next 3 chars "a#b".

Recovered list: ["hello", "world", "", "a#b"].

Handling edge cases

Empty strings in the list: encoded as 0# — decoder will read zero characters and append "".

Strings containing the separator #: fine — the length tells the decoder how many characters belong to the string, so internal # characters don’t confuse it.

Empty list []: encoding produces "" (empty string). Decoding "" returns [] because the while i < len(s) immediately exits.

Non-ASCII characters: len() counts Python string characters (code points). If storing/transmitting as bytes, be mindful of UTF-8 encoding (byte length may differ from character count). This implementation assumes working with Python str objects consistently.

Complexity

Let n be the total number of characters across all strings in the input list and m be the number of strings.

encode:

Time: O(n + m) — you must visit every character and also create length prefixes.
Note: Using res += ... repeatedly is O(n²) if strings are concatenated naively in some languages, but in CPython small repeated concatenation can be amortized; still, it's safer to build with a list and ''.join(...) for large inputs. Best practice: build parts in a list and join.

Space: O(n + size_of_length_digits) for the encoded string.

decode:

Time: O(n) — it walks the encoded string once, parsing lengths and slicing exact substrings.

Space: O(n) for the result list and strings.

Overall asymptotic time is linear in the total encoded size.

Robustness & potential improvements

Concatenation performance:
Replace res += ... with:

parts = []
for s in strs:
    parts.append(str(len(s)) + "#" + s)
return "".join(parts)


This avoids repeated string reallocation and is more efficient for large inputs.

Binary-safe / bytes:
If you need a byte-level protocol (e.g., for network sockets), encode lengths in a fixed-width binary header (e.g., 4 bytes, big-endian) instead of decimal text. That avoids variable-length number parsing and issues with multi-byte encodings.

Validation / error handling:
The decoder assumes well-formed input. For production code you might add bounds checks (ensure j doesn’t run past end, ensure length is non-negative and that j+1+length <= len(s)), and raise descriptive errors if the input is malformed.

Unicode vs byte lengths:
If you serialize to bytes (e.g., UTF-8), remember len(s) in Python counts characters, not bytes. For byte-level protocols use len(s.encode('utf-8')) and store/read bytes.

Summary (one-line)

The encode method writes each string as <length>#<string> and joins them; the decode method reads the length then extracts exactly that many characters — a simple, robust way to serialize a list of strings that allows any character (including the separator) in the string contents.

Want me to:

show a commented version of the code with best-practice join changes,

or provide a binary-header version for byte protocols?
"""


















































