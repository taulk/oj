class Solution(object):
    def toi(self, str):
        numbers="0123456789"
				# read the docs. really cool next(). https://docs.python.org/2/library/functions.html#next
				# see: http://stackoverflow.com/questions/9868653/find-first-list-item-that-matches-criteria
        s = str[:next((i for i in range(len(str)) if str[i] not in '0123456789'), len(str))]
        if len(s) == 0:
            return 0
        return int(s)

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        
        if len(str) == 0:
            return 0
        
        if str[0] == '+':
            return min(self.toi(str[1:]), 0x7fffffff)
        elif str[0] == '-':
            return max(-self.toi(str[1:]), -0x80000000)
        else:
            return max(min(self.toi(str), 0x7fffffff), -0x80000000)
