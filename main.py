import asyncio
import random
import requests
from crawl4ai import BrowserConfig, CrawlerRunConfig, AsyncWebCrawler


def get_proxy():
    no_proxy = True
    print("Getting a proxy...")
    print("Your current IP:\n")

    cur_ip_info = requests.get("https://ipinfo.io/json")
    print(cur_ip_info.text)

    with open("proxies/working_proxies.txt", "r") as f:
        proxies = f.read().splitlines()

    print("Your proxy:\n")
    while no_proxy:
        proxy = random.choice(proxies)
        proxy_info = requests.get(
            "https://ipinfo.io/json",
            proxies={
                "http": proxy,
                "https": proxy
            },
            timeout=10
        )
        if proxy_info.status_code == 200:
            no_proxy = False
    print(proxy_info.text)
    return proxy

async def get_reddit_posts():
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
        proxy=get_proxy()
    )
    crawler_config = CrawlerRunConfig()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.reddit.com/r/AskMen/",
            config=crawler_config
        )

        print(result.markdown) # type: ignore
        with open("result.md", "w") as f:
            f.write(result.markdown) # type: ignore

async def main():
    await get_reddit_posts()

if __name__ == "__main__":
    asyncio.run(main())