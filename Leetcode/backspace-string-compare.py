class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def checkStrings(strings):
            stack = []
            for string in strings:
                if string == "#" and len(stack):
                    stack.pop()
                elif string != "#":
                    stack.append(string)
            return "".join(stack)
        s1 = checkStrings(s)
        s2 = checkStrings(t)
        return s1 == s2
        