class LoginFailedError(Exception):
    """Raised when login to Snoonotes API fails."""
    pass

class RequestFailedError(Exception):
    """Raised when a query to Snoonotes API fails."""
    pass
