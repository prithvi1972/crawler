import datetime
import database
from config import DEFAULT_CRAWL_FREQUENCY


class ValidateCrawlHandler:
    def __init__(self, context=None):
        self.context = context if context is not None else {}

    def validate_last_crawl_time_for_canonical(self):
        url = self.context.get('url')
        if self.context['validate_crawl']['skip_crawl'] is False:
            threshold_time = datetime.datetime.now() - datetime.timedelta(seconds=DEFAULT_CRAWL_FREQUENCY)
            last_crawl_time = database.get_last_crawl_time(url)
            if last_crawl_time and last_crawl_time > threshold_time:
                self.context['validate_crawl']['skip_crawl'] = True

    def validate_last_crawl_time_for_domain(self):
        # politeness logic will come here
        # rate limit on the basis of domain
        pass

    def perform(self):
        self.context['validate_crawl'] = {'skip_crawl': False}
        self.validate_last_crawl_time_for_canonical()
