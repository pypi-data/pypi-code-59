import requests


class Protocol:
    __protocol: str

    def __init__(self, protocol: str):
        self.__protocol = protocol

    def __str__(self) -> str:
        return self.__protocol + '://'

    def __add__(self, other) -> str:
        return str(self) + other


class Domain:
    __domain: str

    def __init__(self, domain: str):
        self.__domain = domain

    def __str__(self) -> str:
        return self.__domain

    def __add__(self, other) -> str:
        return str(self) + other


class BillingApiUrl:
    __url: str

    def __init__(self, url: str):
        self.__url = url

    def __str__(self) -> str:
        return self.__url

    def __add__(self, other) -> str:
        return str(self) + other


class HostGatewayUrl:
    __url: BillingApiUrl
    __domain: Domain

    def __init__(self, url: BillingApiUrl, domain: Domain):
        self.__url = url
        self.__domain = domain

    def __str__(self) -> str:
        return self.__url + '/host/' + str(self.__domain)


class Url:
    """Url - is url for clinic address lile https://myclinic.host.name """

    def __init__(self):
        raise NotImplementedError


class UrlFromGateway(Url):
    __host_gateway_url: HostGatewayUrl
    __response_json = None

    def __init__(self, host_gateway_url: HostGatewayUrl):
        self.__host_gateway_url = host_gateway_url

    def __invalid_response(self):
        return 'success' not in self.response_json \
               or 'url' not in self.response_json \
               or self.response_json['success'] is False

    def __str__(self) -> str:
        if self.__response_json is None:
            response = requests.get(str(self.__host_gateway_url))
            self.response_json = response.json()
        if self.__invalid_response():
            raise Exception(
                'Invalid response from Host Gateway : {}'.format(response.text)
            )
        return Protocol(
            self.response_json['protocol']
        ) + self.response_json['url']

    def __add__(self, other) -> str:
        return str(self) + other


class FakeUrl(Url):

    def __init__(self):
        pass

    def __str__(self) -> str:
        return 'http://fake.url'

    def __add__(self, other) -> str:
        return str(self) + other
