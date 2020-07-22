import unittest
from vetmanager.url import Url, FakeUrl
from vetmanager.token import Credentials, Token
from vetmanager.functions import url, token_credentials, token


class TestFunctions(unittest.TestCase):
    def test_url(self):
        self.assertTrue(
            isinstance(url('test'), Url)
        )

    def test_credentials(self):
        self.assertTrue(
            isinstance(
                token_credentials(
                    login='test',
                    password='test',
                    app_name='test'
                ),
                Credentials
            )
        )

    def test_token(self):
        self.assertTrue(
            isinstance(
                token(
                    FakeUrl(),
                    token_credentials(
                        login='test',
                        password='test',
                        app_name='test'
                    )
                ),
                Token
            )
        )


if __name__ == '__main__':
    unittest.main()
