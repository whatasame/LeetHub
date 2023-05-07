class Solution(object):
    def romanToInt(self, s):
        val_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        replace_dict = {
            "IV" : "IIII",
            "IX" : "VIIII",
            "XL" : "XXXX",
            "XC" : "LXXXX",
            "CD" : "CCCC",
            "CM" : "DCCCC"
        }

        for k, v in replace_dict.items():
            s = s.replace(k,v)
        
        answer = 0
        for c in s:
            answer += val_dict[c]

        return answer