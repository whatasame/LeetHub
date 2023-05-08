class Solution(object):
    def compare(self, i, strs):
        if i >= len(strs[0]):
            return ""
        c = strs[0][i]

        for s in strs:
            if i >= len(s) or s[i] != c:
                return ""

        return c

    def longestCommonPrefix(self, strs):
        # compare digit 0 to 200 of strs
        results = []
        for i in range(201):
            results.append(self.compare(i, strs))

        # output
        answer = []
        for result in results:
            if result == "":
                break
            answer.append(result)
        return "".join(answer)