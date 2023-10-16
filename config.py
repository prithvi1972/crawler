import os

USER_AGENT = 'PostmanRuntime/7.33.0'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_DB_PATH = os.path.join(ROOT_DIR, 'db', 'html.db')
METADATA_DB_PATH = os.path.join(ROOT_DIR, 'db', 'metadata.db')

DEFAULT_CRAWL_FREQUENCY = 86400  # in second(s)
