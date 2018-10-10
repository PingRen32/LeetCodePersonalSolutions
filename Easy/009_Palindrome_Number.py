class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Larger than 0 to be valid
        if x >= 0:
            # Single digit are all considered true
            if x <= 9:
                return True
            else:
                # Turn int into string
                s = str(x)
                # Reverse the string and turn back int
                res = int(s[::-1])
                # Return true if match
                return True if res == x else False
        else:
            return False