import concurrent.futures
from chain.CrawlerChain import CrawlerChain
import database
import os


def init_app(reset_db=False):
    if reset_db:
        if os.path.exists(database.METADATA_DB_PATH):
            os.remove(database.METADATA_DB_PATH)
        if os.path.exists(database.HTML_DB_PATH):
            os.remove(database.HTML_DB_PATH)
    database.create_html_table()
    database.create_metadata_table()


def crawl(url):
    context = {'url': url}
    CrawlerChain().execute(context)
    return context['metadata']


def sync(urls):
    for url in urls:
        print(crawl(url))


def concur(urls):
    executor = concurrent.futures.ThreadPoolExecutor()
    results = executor.map(crawl, urls)
    for result in results:
        print(result)


# change reset_db to True to flush DBs on server start
init_app(reset_db=False)

test_urls = [
    "http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster",
    "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/",
    "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"
]

sync(test_urls)
