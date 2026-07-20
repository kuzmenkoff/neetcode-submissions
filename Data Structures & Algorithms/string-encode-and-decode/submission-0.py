class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for word in strs:
            code += str(len(word)) + '#' + word
        return code

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                count_str = ""
                while s[i] != '#':
                    count_str += s[i]
                    i = i + 1
                i = i + 1
                start = i
                end = start + int(count_str)
                word = s[start:end]
                result.append(word)
                i = end 
        return result
