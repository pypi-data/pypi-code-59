from base64 import b64encode

class BasicAuth:
    """Class to create a BasicAuth-style header dictionary for use with
    BasicAuth API's.

    Parameters:
        appKey: string
        The API key as given to you by the API provider
    """

    def __init__(self, user, key=False):
        "Converts appKey to bites and executes buildHeader method"

        self.user = bytes(user,"utf-8")

        if key:
            self.key  = bytes(key,"utf-8")
        else:
            self.key = key

        self.buildHeader()

    def buildHeader(self):
        """Creates a basic auth header, by encoding bytes to base64 and then
        decoding to ascii.

        Has format "Authorization": "Basic <ascii-decoded key>" per the standard

        Note that it does not currently support basic auth use cases where a
        password is also required.

        Creates attribute self.basicAuthHeader

        Arguments: none
        """
        if self.key:
            userString = self.user+b":"+self.key
        else:
            userString = self.user+b":"
            
        encodedUserString = b64encode(userString)
        decodedUserString = encodedUserString.decode("ascii")
        self.basicAuthHeader = {"Authorization": "Basic " + decodedUserString}
