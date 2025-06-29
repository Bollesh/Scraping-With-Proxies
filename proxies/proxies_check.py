import threading
import requests
from queue import Queue
import time

q = Queue()

with open("proxies.txt", "r") as f:
    all_proxies = f.read().splitlines()
    for p in all_proxies:
        q.put(p)

working_proxies = []

def checker():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get(
                "https://www.reddit.com/",
                proxies={
                    "http": proxy,
                    "https": proxy
                },
                timeout=15
            )
        except:
            continue

        if res.status_code == 200:
            working_proxies.append(proxy)
            print(res.text)

threads = []

for _ in range(100):
    thread = threading.Thread(target=checker)
    thread.start()
    threads.append(thread)

for t in threads:
    thread.join()
    
time.sleep(30)

with open("working_proxies.txt", "w") as f:
    f.write("\n".join(working_proxies))