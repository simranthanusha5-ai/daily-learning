# Day 99 Project: URL Shortener and Base62 Encoder
import string

class URLShortener:
    BASE62 = string.digits + string.ascii_letters

    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.counter = 1000

    def shorten(self, url: str) -> str:
        if url in self.url_to_code:
            return self.url_to_code[url]
        code = self._encode_base62(self.counter)
        self.counter += 1
        self.url_to_code[url] = code
        self.code_to_url[code] = url
        return code

    def _encode_base62(self, num: int) -> str:
        chars = []
        while num > 0:
            chars.append(self.BASE62[num % 62])
            num //= 62
        return "".join(reversed(chars))

shortener = URLShortener()
code = shortener.shorten("https://github.com/simranthanusha5-ai/daily-learning")
print(f"Shortened code: https://short.ly/{code}")
