"""
Given a 32-bit signed integer, reverse digits of an integer.
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        X = str(abs(x))
        Y = X[-1]
        for i in range(1,len(X)):
            Y += X[len(X)-i-1]
        if x>2**31 -1 or x<-2**31:
            y = 0
        else:
            y = int(Y)
        
        if x<0:
            y = -y
        
        #注意：y也应该在 [−2^31,  2^31 − 1]范围中！     
        if y>2**31 -1 or y<-2**31:
            y = 0 
        return y