from bs4 import BeautifulSoup
import database


class ExtractMetadataHandler:
    def __init__(self, context=None):
        self.context = context if context is not None else {}

    def perform(self):
        html_id = self.context.get('html', {}).get('id')
        html = database.get_html_content_by_id(html_id)
        if html:
            try:
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.title.string if soup.title else None
                description = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={
                    'name': 'description'}) else None
                body = soup.get_text()
                metadata_id = database.persist_metadata(title, description, body)
                self.context['metadata'] = {
                    'id': metadata_id,
                    'title': title,
                }
                return
            except Exception as e:
                print(f"An error occurred while extracting metadata: {e}")
        self.context['metadata'] = None
