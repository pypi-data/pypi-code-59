import json
import requests
import base64
import os

API_BAS_URL = 'https://app.postbode.nu/api'
HEADERS = {'Content-Type': 'application/json'}


class Client(object):

    def __init__(self, api_token: str):
        """Instantiate Postbode API client.

        :param api_base_url: API url starting point
        :type api_base_url: str
        :param token: API Token
        :type token: str
        :param mailbox: Mailbox id
        :type mailbox: str
        """

        self.api_base_url = API_BAS_URL
        self.headers = HEADERS

        # prepare header with authorization token.
        self.headers['X-Authorization'] = api_token

    """
    Helper methods
    """

    def hash_document(self, filepath) -> str:
        """Base64 encode PDF file.

        :param filepath: The file to use
        :type filepath: str.
        :returns: str of hashed file.
        """
        with open(filepath, 'rb') as document:
            encoded_string = base64.b64encode(document.read()).decode("utf-8")
        return encoded_string

    def file_name_check(self, doc_name) -> str:
        """Get filename.

        :param doc_name: Full name of document
        :type doc_name: str.
        :returns: str of filename base.

        """
        if doc_name == '':
            self.send_letter.doc_file = os.path.splitext(
                self.send_letter.doc_file)[0]
        else:
            return doc_name

    def get_mailboxes(self):
        """
        Get all available mailboxes of token.
        """
        url = '{}/mailbox'.format(self.api_base_url)
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return print('[!] HTTP {} calling {} with headers {}'.format(response.status_code, url, self.headers))

    def get_letters(self, mailbox):
        """
        Get letter information.
        """
        url = '{}/mailbox/{}'.format(self.api_base_url, mailbox)
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return print('[!] HTTP {} calling {} with headers {}'.format(response.status_code, url, self.headers))

    def send_letter(self,
                    mailbox_id,
                    doc_name,
                    doc_file,
                    envelope_id,
                    country,
                    registered,
                    color,
                    printing,
                    printer,
                    send):
        """Send a letter."""

        url = '{}/mailbox/{}/letters'.format(self.api_base_url, mailbox_id)

        payload = {'documents': [{'name': doc_name, 'content': self.hash_document(doc_file)}], 'envelope_id': envelope_id,
                   'country': country, 'registered': registered, 'color': color, 'printing': printing, 'printer': printer, 'send': send}

        request = requests.post(url, headers=self.headers, json=payload)

        if request.status_code == 200:
            return json.loads(request.content)
        else:
            return print('[!] HTTP {} calling {} with headers {}'.format(request.status_code, url, self.headers))

    def send_letters(self,
                     mailbox_id,
                     envelope_id,
                     country,
                     registered,
                     color,
                     printing,
                     printer,
                     send,
                     *docs):
        """Send multiple letters at once.

        example: 
        letters = ('./file1', './file2')
        client.send_letters(2522, 2, 'NL', False, 'FC', 'simplex', 'inkjet', True, *letters)
        """
        url = '{}/mailbox/{}/letters'.format(self.api_base_url, mailbox_id)

        print('>> docs: {}'.format(docs))

        for doc in docs:
            print('>> doc: {}'.format(doc))

            payload = {'documents': [{'name': self.file_name_check(doc), 'content': self.hash_document(doc)}], 'envelope_id': envelope_id,
                       'country': country, 'registered': registered, 'color': color, 'printing': printing, 'printer': printer, 'send': send}

            request = requests.post(url, headers=self.headers, json=payload)

            if request.status_code == 200:
                print(json.loads(request.content))
            else:
                print('[!] HTTP {} calling {} with headers {}'.format(
                    request.status_code, url, self.headers))
