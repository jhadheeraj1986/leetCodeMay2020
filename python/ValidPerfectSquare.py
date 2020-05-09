'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

'''

def isPerfectSquare1( num: int) -> bool:
        a = num**0.5
        if a == int(a):
            return True
        else:
            return False


def isPerfectSquare2(self, num: int) -> bool:
    l = 1
    r = num
    while(r >= l):
        mid = int((l + r) / 2)
        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            r = mid - 1
        else:
            l = mid + 1
    return False


def isPerfectSquare3(self, num: int) -> bool:
        if num < 2:
            return True
        
        left, right = 2, num //2
        while left <= right:
            mid = (left + right) // 2
            guess_sq = mid * mid
            if guess_sq == num:
                return True
            elif guess_sq > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False




