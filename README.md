# Web Crawling Application

This Python application is designed to crawl web pages, fetch HTML content, and extract metadata. It uses a chain of handlers to process web pages, and the data is stored in a SQLite database for future reference.

## Features

- **Web Crawling:** The application can crawl web pages using the provided URLs.

- **Metadata Extraction:** It extracts metadata such as the page title and description from the HTML content.

- **Database Storage:** Metadata and HTML content are stored in a SQLite database for future use.

- **Concurrency:** It supports concurrent crawling of multiple URLs for faster processing.

- **Rate Limiting:** The application prevents over-crawling by checking the last crawl time of URLs and Domains(WIP).

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.x installed on your system.
- The required Python packages installed. You can install them using `pip`:

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/prithvi1972/crawler.git
cd crawler
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python main.py
```

The application will start crawling the provided test URLs. You can add more URLs to the `test_urls` list in the `main.py` file.

## Configuration

The application's behavior can be configured in the `config.py` file. You can adjust parameters such as the user agent, database paths, and crawl frequency.

## Database

The application uses two SQLite databases for storing data: `metadata.db` for metadata and `html.db` for HTML content. If you want to reset the databases, set `reset_db` to `True` in `main.py`.
