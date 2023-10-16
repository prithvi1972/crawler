import sqlite3
from config import METADATA_DB_PATH, HTML_DB_PATH
from datetime import datetime


def execute_sql(db_path, sql, values=None, return_last_row_id=False):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            if values:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)

            if sql.upper().strip().startswith('SELECT'):
                result = cursor.fetchall()
                return result
            else:
                conn.commit()

                if return_last_row_id:
                    return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


def create_metadata_table():
    sql = '''
        CREATE TABLE IF NOT EXISTS metadata (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            body TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    '''
    execute_sql(METADATA_DB_PATH, sql)


def create_html_table():
    sql = '''
        CREATE TABLE IF NOT EXISTS html (
            id INTEGER PRIMARY KEY,
            content TEXT,
            url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    '''
    execute_sql(HTML_DB_PATH, sql)
    # Index
    index_sql = 'CREATE INDEX IF NOT EXISTS url_index ON html (url);'
    execute_sql(HTML_DB_PATH, index_sql)


def persist_metadata(title, description, body):
    sql = '''
        INSERT INTO metadata (title, description, body)
        VALUES (?, ?, ?)
    '''
    values = (title, description, body)
    return execute_sql(METADATA_DB_PATH, sql, values, return_last_row_id=True)


def persist_html(content, url):
    sql = '''
        INSERT INTO html (content, url)
        VALUES (?, ?)
    '''
    values = (content, url)
    return execute_sql(HTML_DB_PATH, sql, values, return_last_row_id=True)


def get_html_content_by_id(html_id):
    try:
        sql = 'SELECT content FROM html WHERE id = ?'
        values = (html_id,)
        result = execute_sql(HTML_DB_PATH, sql, values)
        if result:
            return result[0][0]
        else:
            return None
    except sqlite3.Error as e:
        print(f"An error occurred while retrieving HTML from the database: {e}")
        return None


def get_last_crawl_time(url):
    sql = 'SELECT MAX(created_at) FROM html WHERE url = ?'
    values = (url,)
    last_crawl_time_str = execute_sql(HTML_DB_PATH, sql, values)

    if last_crawl_time_str and last_crawl_time_str[0]:
        last_crawl_time_str = last_crawl_time_str[0][0]
        if last_crawl_time_str is None:
            return last_crawl_time_str
        last_crawl_time = datetime.strptime(last_crawl_time_str, "%Y-%m-%d %H:%M:%S")
        return last_crawl_time
    else:
        return None
