"""Day 268: Mini Regex Matcher."""

def match_star(char, pattern, text):
    while text and (text[0] == char or char == '.'):
        if match_regex(pattern, text):
            return True
        text = text[1:]
    return match_regex(pattern, text)

def match_regex(pattern, text):
    if not pattern:
        return True
    if len(pattern) >= 2 and pattern[1] == '*':
        return match_star(pattern[0], pattern[2:], text)
    if text and (pattern[0] == '.' or pattern[0] == text[0]):
        return match_regex(pattern[1:], text[1:])
    return False

if __name__ == "__main__":
    assert match_regex("a*b", "aaab") is True
    assert match_regex("a*b", "ac") is False
    assert match_regex("a.c", "abc") is True
    print("Day 268 Regex tests passed!")
