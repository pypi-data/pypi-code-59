import os
import warnings
import urllib3


def set(skip_verify: bool) -> None:
    """Switch SSL verification.

    Parameters
    ----------
    skip_verify : bool
        True: skip,
        False: verify
    """
    if skip_verify:
        os.environ["CURL_CA_BUNDLE"] = ""
        warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)
    else:
        os.environ.pop("CURL_CA_BUNDLE", None)
        warnings.simplefilter("default", urllib3.exceptions.InsecureRequestWarning)
