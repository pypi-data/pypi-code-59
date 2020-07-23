#######################
## Public exceptions
#######################
class NBSRbaseException(Exception):
    """Base exception in the NBSR package and all other exceptions are sub-classes"""
    pass

class NonStreamException(NBSRbaseException):
    """The stream is expected to be a file-type object"""
    pass

class StreamUnexpectedlyClosed(NBSRbaseException):
    """The stream got closed while we were reading it"""
    pass

class WorkerRunningException(NBSRbaseException):
    """Cannot start NBSR worker twice"""
    pass

class ReadException(NBSRbaseException):
    """Reading attempt before starting NBSR worker"""
    pass

class rePatternError(NBSRbaseException):
    """The pattern received cannot be compiled"""
    pass


#######################
## Private exceptions
#######################
class _TimeOutOccured(NBSRbaseException):
    """No (enough) data could be read from the stream"""
    pass
