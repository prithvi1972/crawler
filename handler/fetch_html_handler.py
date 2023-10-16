import requests
from config import USER_AGENT
import database


class FetchHtmlHandler:
    def __init__(self, context=None):
        self.context = context if context is not None else {}

    def perform(self):
        url = self.context.get('url')

        if self.context.get('validate_crawl', {}).get('skip_crawl', True):
            print(f"Skipping crawl for {url} as it was crawled recently.")
            return

        try:
            headers = {'User-Agent': USER_AGENT}
            session = requests.Session()
            response = session.get(url, headers=headers)
            response.raise_for_status()
            html_id = database.persist_html(response.text, url)
            self.context['html'] = {'id': html_id}
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching HTML for {url}: {e}")
            self.context['html'] = None
