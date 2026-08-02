# Day 52: Stack & Parentheses Validation

def is_valid_parentheses(s: str) -> bool:
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return len(stack) == 0

print("Test '[{()}]':", is_valid_parentheses("[{()}]"))
print("Test '[(])':", is_valid_parentheses("[(])"))
