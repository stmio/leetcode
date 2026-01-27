class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if p in ["(", "[", "{"]:
                stack.append(p)
                continue

            if len(stack) == 0:
                return False

            opening = stack.pop()

            if opening == "(" and p != ")":
                return False
            if opening == "[" and p != "]":
                return False
            if opening == "{" and p != "}":
                return False
                
        return len(stack) == 0