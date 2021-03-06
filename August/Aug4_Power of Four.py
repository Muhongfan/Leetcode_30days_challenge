"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""


def isPowerOfFour(self, num: int) -> bool:
    if num <= 0:
        return False
    if num == 1:
        return True
    if (num - 1) % 3 == 0 and num & (num - 1) == 0:
        return True
    else:
        return False