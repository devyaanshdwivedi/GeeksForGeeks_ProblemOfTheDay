class Solution:
    def printMinNumberForPattern(self, S):
        result = ""
        stack = []
        current_number = 1

        for i in range(len(S) + 1):
            stack.append(current_number)

            if i == len(S) or S[i] == 'I':
                while stack:
                    result += str(stack.pop())

            current_number += 1

        return result