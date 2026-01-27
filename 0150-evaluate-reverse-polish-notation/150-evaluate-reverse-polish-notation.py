class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t.isnumeric() or t[1:].isnumeric():
                stack.append(int(t))
                continue

            a = stack.pop()
            b = stack.pop()

            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(b - a)
            elif t == "*":
                stack.append(a * b)
            else:
                stack.append(int(b/a))

        return stack.pop()