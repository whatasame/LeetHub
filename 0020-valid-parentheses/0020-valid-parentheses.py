class Solution(object):
    def isValid(self, s):
        pair = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []  # stack
        for b in s:  # bracket
            if b in pair:
                stack.append(b)
            # no more pair or no match pair:
            elif len(stack) == 0 or pair[stack.pop()] != b:
                return False

        return len(stack) == 0
        