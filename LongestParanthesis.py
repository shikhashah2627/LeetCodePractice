class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, longest, index = [0], 0, 0    
        for index in range(0, len(s)):
            if s[index] == ")" and len(stack) != 1:
                length, last = stack.pop(), stack.pop()
                total_length = last + length + 2
                stack.append(total_length)
                longest = max(longest, total_length)
            elif s[index] == "(":
                stack.append(0)
            else:
                stack = [0]
        
        return longest