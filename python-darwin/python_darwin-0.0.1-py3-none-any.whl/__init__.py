

import requests
from requests.compat import urljoin
from lxml import html

from darwin.exceptions import DarwinHttpError, DarwinError


__title__ = "python-darwin"
__version__ = "0.0.1"
__author__ = "Roald Nefs"
__email__ = "info@roaldnefs.com"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2020 Roald Nefs <info@roaldnefs.com>"


# Default URL for the Darwin data source
DEFAULT_URL = "https://duitseherder.nl/leden/darwin" 

class Darwin(object):
    """Represents a Darwin connection.
    
    Args:
        url (str): The URL of Darwin.
    """
    
    def __init__(self, url=DEFAULT_URL):
        self.url = url
        # Update the user agent
        self.headers = {"User-Agent": "{}/{}".format(__title__, __version__)}

    def _get_headers(self):
        """Update the default requests headers with the custom ones.
        
        Returns:
            A dictionary containing the updated headers.
        """
        headers = requests.utils.default_headers()
        headers.update(self.headers)
        return headers

    def _build_payload(self, query=None, page=None):
        """Return the payload based on the supplied query.

        Args:
            query (str): The search query.
            page (int): The result page.

        Returns:
            A dictionary containing the supplied search query or None otherwise.
        """
        if query:
            page = page if page else 1
            return {
                'search[158f653e50fee1c614785ac6c8cffcff]': query,
                'page[158f653e50fee1c614785ac6c8cffcff]': page
               }

    def _build_url(self, path=None):
        """Returns the full URL from path.

        If the path is supplied, the combined base URL and path are returned
        otherwise the base URL is returned.

        Returns:
            The full URL. 
        """
        return urljoin(self.url, path)


    def query(self, query):
        """Perform a search query on Darwin.

        Raises:
            DarwinError: When Darwin returns a error message.
            DarwinHttpError: When the return code is not 200.

        Returns:
            Dictionary containing all dogs matching the search query.
        """
        path = self._build_url()
        # Holds all dogs matching the search query
        dogs = []
        page = 1

        # Keep combining all pages until the last page has been scraped
        while True:
            payload = self._build_payload(query=query, page=page)

            # Perform the actual request
            result = self._http_request(path, payload=payload)
            tree = html.fromstring(result.content)

            # Check for an error message in the content
            errors = tree.xpath('//div[contains(@class, "alert") and contains(@class, "alert-danger")]/text()')
            if errors:
                raise DarwinError(
                    error_message=errors[0],
                    response_code=result.status_code,
                    response_body=result.content
                )

            # Scrape all information on the current page
            items = tree.xpath('//div[contains(@id, "158f653e50fee1c614785ac6c8cffcff") and contains(@class, "itemOverview")]//div[@class="itemLink"]/a')
            for item in items:
                name = next(iter(item.xpath('h2[@class="itemHeading"]/text()')), None)
                link = next(iter(item.xpath('@href')), None)
                date_of_birth = next(iter(item.xpath('span[contains(@class, "field_gebdate")]/text()')), None)
                studbook_id = next(iter(item.xpath('span[contains(@class, "field_dogId")]/text()')), None)

                dogs.append({
                    "name": name,
                    "link": link,
                    "date_of_birth": date_of_birth,
                    "id": studbook_id,
                    "page": page
                })

            # Check if the last page has been reached
            next_page = next(iter(tree.xpath('//ul[contains(@class, "pagination") and contains(@class, "itemPagination")]//li[@class="itemNext"]//a/@href')), None)
            if next_page is None or next_page == '#':
                break
            page += 1

        return dogs

    def _http_request(self, path, payload=None):
        """Make a HTTP request to Darwin.

        Raises:
            DarwinHttpError: When the return code is not 200.

        Returns:
            A requests result object.
        """
        result = requests.get(
            path,
            params=payload,
            headers=self._get_headers()
        )

        # Return the requests result object if the status code of the request
        # is 200
        if result.status_code == 200:
            return result

        raise DarwinHttpError(
            error_message="",  # TODO
            response_code=result.status_code,
            response_body=result.content
        )
        

    