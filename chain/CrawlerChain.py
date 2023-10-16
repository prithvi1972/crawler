from lib.ChainInterface import ChainInterface

from handler.fetch_html_handler import FetchHtmlHandler
from handler.extract_metadata_handler import ExtractMetadataHandler
from handler.validate_crawl_handler import ValidateCrawlHandler


class CrawlerChain(ChainInterface):
    def __init__(self):
        super().__init__([
            ValidateCrawlHandler,
            FetchHtmlHandler,
            ExtractMetadataHandler
        ])
