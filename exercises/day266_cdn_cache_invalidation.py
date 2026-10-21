"""Day 266: CDN Cache Invalidation."""

class CDNCache:
    def __init__(self):
        self.cache = {} # url -> content
        self.tags = {}  # tag -> set of urls

    def put(self, url, content, tags=()):
        self.cache[url] = content
        for t in tags:
            self.tags.setdefault(t, set()).add(url)

    def purge_tag(self, tag):
        urls = self.tags.pop(tag, set())
        for u in urls:
            self.cache.pop(u, None)

if __name__ == "__main__":
    cdn = CDNCache()
    cdn.put("/product/1", "Shoes", tags=["products", "apparel"])
    cdn.put("/product/2", "Hat", tags=["products", "apparel"])
    cdn.purge_tag("products")
    assert "/product/1" not in cdn.cache
    print("Day 266 CDN Invalidation tests passed!")
