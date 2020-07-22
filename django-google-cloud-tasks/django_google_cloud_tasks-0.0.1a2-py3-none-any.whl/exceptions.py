class GoogleCredentialsException(Exception):
    def __init__(self):
        message = 'GCP_B64 or GOOGLE_APPLICATION_CREDENTIALS env variable not set properly'
        super().__init__(message)
