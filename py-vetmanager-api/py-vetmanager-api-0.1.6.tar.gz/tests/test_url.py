import unittest
from unittest import mock
from .mock import MockResponse
from vetmanager.url import Protocol, Domain, Url, \
    BillingApiUrl, HostGatewayUrl, UrlFromGateway


class TestUrl(unittest.TestCase):

    def test_protocol(self):
        self.assertEqual(
            str(
                Protocol('http')
            ),
            'http://'
        )

    def test_domain(self):
        self.assertEqual(
            str(
                Domain('test')
            ),
            'test'
        )

    def test_billing_api_url(self):
        self.assertEqual(
            str(
                BillingApiUrl('http://some.test')
            ),
            'http://some.test'
        )

    def test_host_gateway_url(self):
        gateway_url = str(
            HostGatewayUrl(
                BillingApiUrl("http://test.url"),
                Domain('test')
            )
        )
        self.assertTrue(
            ("http://test.url" in gateway_url) and
            ("test" in gateway_url)
        )

    @mock.patch('vetmanager.url.requests.get')
    def test_host_name_from_gateway_url_valid_response(self, mock):
        mock.return_value = MockResponse({
            "success": True,
            "host": ".testhost.test",
            "url": "test.testhost.test",
            "protocol": "http"
        })

        host_name = UrlFromGateway(
            HostGatewayUrl(
                'http://fake.url',
                Domain('domain')
            )
        )
        self.assertEqual(str(host_name), 'http://test.testhost.test')

    @mock.patch('vetmanager.url.requests.get')
    def test_host_name_from_gateway_url_invalid_response(self, mock):
        mock.return_value = MockResponse({
            "fake": "response"
        })
        with self.assertRaises(Exception):
            str(
                UrlFromGateway(
                    HostGatewayUrl(
                        'http://fake.url',
                        Domain('domain')
                    )
                )
            )

    @mock.patch('vetmanager.url.requests.get')
    def test_host_name_from_gateway_url_invalid_response2(self, mock):
        mock.return_value = MockResponse({
            "success": False,
            "url": "test"
        })
        with self.assertRaises(Exception):
            str(
                UrlFromGateway(
                    HostGatewayUrl(
                        'http://fake.url',
                        Domain('domain')
                    )
                )
            )

    def test_init_host_name_raise_error(self):
        with self.assertRaises(NotImplementedError):
            Url()


if __name__ == '__main__':
    unittest.main()
