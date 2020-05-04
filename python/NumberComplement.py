'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
'''
#Solution 1:
def findComplement(num):
    binNum = bin(num)
    print(type(binNum))
    strbin = binNum[2:]
    strComp = ""
    for c in strbin:
        compC = '1' if c == '0' else '0' 
        strComp = strComp + compC
    #print(strComp)
    comp = int(strComp, 2)
    return comp

#Solution 2:
def findComplement(self, num: int) -> int:
        c = 1
        while num*2 > c:
            num = num ^ c
            c = c << 1

        return num
