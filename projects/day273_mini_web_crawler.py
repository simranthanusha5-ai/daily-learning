"""Day 273: Mini Async Web Crawler."""
import asyncio

class CrawlFrontier:
    def __init__(self, max_pages=5):
        self.queue = asyncio.Queue()
        self.visited = set()
        self.max_pages = max_pages

    async def add_url(self, url):
        if url not in self.visited and len(self.visited) < self.max_pages:
            self.visited.add(url)
            await self.queue.put(url)

    async def worker(self, crawl_log):
        while not self.queue.empty():
            url = await self.queue.get()
            crawl_log.append(url)
            self.queue.task_done()

async def run_crawler():
    frontier = CrawlFrontier()
    log = []
    await frontier.add_url("https://example.com/a")
    await frontier.add_url("https://example.com/b")
    await frontier.worker(log)
    return log

if __name__ == "__main__":
    res = asyncio.run(run_crawler())
    assert len(res) == 2
    print("Day 273 Web Crawler tests passed!")
