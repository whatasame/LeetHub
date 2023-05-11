class Solution(object):
    def strStr(self, haystack, needle):
        answer = -1

        for i in range(len(haystack)):
            if answer != -1: # found idx
                break;

            # brute force
            if haystack[i] == needle[0]:
                answer = i
                for j in range(1, len(needle)):
                    if i + j >= len(haystack) or haystack[i + j] != needle[j]:
                        answer = -1
                        break

        return answer