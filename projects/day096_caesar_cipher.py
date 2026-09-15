# Day 96 Project: Caesar Cipher

def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)

original = "Python Daily Learning Streak!"
encrypted = caesar_cipher(original, shift=4)
decrypted = caesar_cipher(encrypted, shift=4, decrypt=True)

print("Original: ", original)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
assert original == decrypted
