class Solution(object):
    def plusOne(self, digits):
        num = int("".join(map(str,digits)))
        return list(map(int, str(num + 1)))