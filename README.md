# Reddit Proxy Crawler

## Description

This project is a Python-based web crawler that fetches posts from the Reddit website using an asynchronous approach with the help of `Crawl4AI`. The crawler utilizes proxy servers to bypass IP restrictions and ensure smooth operation. It also includes a script for checking the validity of a list of proxies. This concept can be used to scrape other websites as well, Reddit was just used as an example

## Features

- **Asynchronous Web Crawling**: Uses `asyncio` for efficient, non-blocking operations.
- **Proxy Management**: Dynamically selects working proxies from a provided list.
- **Reddit Post Scraping**: Fetches and saves Reddit posts in Markdown format.
- **Threaded Proxy Validation**: Efficiently checks the validity of multiple proxies concurrently.

## Installation

To set up this project, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo-url.git
   cd your-repo-name/project
   ```

2. Install the required dependencies using `pip`:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Crawler


To run the crawler, execute the following command:

```sh
python main.py
```

This will fetch Reddit posts and save them in a Markdown file named `result.md`.

### Validating Proxies

The proxy validation script can be run separately to ensure that only working proxies are used. To do this, navigate to the `proxies` directory and execute:

```sh
cd project/proxies
python proxies_check.py
```

This will check the validity of all proxies in `proxies.txt` and save the working ones in `working_proxies.txt`.

Note - Provide your own proxy servers. Write them to "proxies.txt"

## Project Structure

The project is organized as follows:

- **main.py**: The main script for fetching Reddit posts using an asynchronous crawler.
- **requirements.txt**: A list of required Python packages.
- **project/proxies/**: Contains scripts for proxy validation.

```
project/
├── main.py
├── requirements.txt
└── proxies/
    └── proxies_check.py
```

## Dependencies

The project relies on the following libraries:

```plaintext
aiofiles==24.1.0
aiohappyeyeballs==2.6.1
aiohttp==3.12.13
aiosignal==1.3.2
aiosqlite==0.21.0
annotated-types==0.7.0
anyio==4.9.0
attrs==25.3.0
beautifulsoup4==4.13.4
Brotli==1.1.0
certifi==2025.6.15
cffi==1.17.1
chardet==5.2.0
charset-normalizer==3.4.2
click==8.2.1
colorama==0.4.6
Crawl4AI==0.6.3
cryptography==45.0.4
cssselect==1.3.0
distro==1.9.0
fake-http-header==0.3.5
fake-useragent==2.2.0
filelock==3.18.0
frozenlist==1.7.0
fsspec==2025.5.1
greenlet==3.2.3
h11==0.16.0
hf-xet==1.1.5
httpcore==1.0.9
httpx==0.28.1
huggingface-hub==0.33.1
humanize==4.12.3
idna==3.10
importlib_metadata==8.7.0
Jinja2==3.1.6
jiter==0.10.0
joblib==1.5.1
jsonschema==4.24.0
jsonschema-specifications==2025.4.1
litellm==1.73.2
lxml==5.4.0
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
multidict==6.6.1
nltk==3.9.1
numpy==2.3.1
openai==1.93.0
packaging==25.0
pillow==10.4.0
playwright==1.53.0
propcache==0.3.2
psutil==7.0.0
pycparser==2.22
pydantic==2.11.7
pydantic_core==2.33.2
pyee==13.0.0
Pygments==2.19.2
pyOpenSSL==25.1.0
pyperclip==1.9.0
python-dotenv==1.1.1
PyYAML==6.0.2
rank-bm25==0.2.2
referencing==0.36.2
regex==2024.11.6
requests==2.32.4
rich==14.0.0
rpds-py==0.25.1
sniffio==1.3.1
snowballstemmer==2.2.0
soupsieve==2.7
tf-playwright-stealth==1.2.0
tiktoken==0.9.0
tokenizers==0.21.2
tqdm==4.67.1
typing-inspection==0.4.1
typing_extensions==4.14.0
urllib3==2.5.0
xxhash==3.5.0
yarl==1.20.1
zipp==3.23.0
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Feel free to explore, contribute, and enhance this project! 🚀
