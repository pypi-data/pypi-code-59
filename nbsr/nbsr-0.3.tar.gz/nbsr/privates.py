"""NBSR private methods in a Mixin class"""


import sys
import queue
import re
import functools
import inspect
from wrapt import decorator
from .exceptions import StreamUnexpectedlyClosed, _TimeOutOccured, rePatternError
from .returnbys import *


def _separate_args(wrapped, wrapped_argslen, wrapper_args_def, args, kwargs):
    """Separate wrapper and wrapped function arguments
    
    Args:
        wrapped (function object): the wrapped function
        wrapped_argslen (int): the length of the wrapped function args
        wrapper_args_def (tuple): definition of list of arguments which are used by
            the wrapper only. Each such argument is defined by a dict with keys of
            ``name`` and ``default``.
        args: the positional arguments tuple received in the wrapper
        kwargs: the keyword arguments dict received in the wrapper
    
    Returns:
        tuple: 3 elements: the remaining args and the remaining kwargs
        after wrapper argument extraction and the separated wrapper kwargs
    """
    #create an empty dict for collecting wrapper keyword arguments
    wrapper_kwargs = dict()
    
    #separate the positional args for the wrapped function
    funcargs = args[:wrapped_argslen]
    
    #separation is needed, if arguments are defined for the wrapper
    if wrapper_args_def is not None:
        #separate the positional args for the wrapper
        wrapper_arg_vals = list(args[wrapped_argslen:])
        
        #loop on all wrapper argument names
        for wrapper_arg in wrapper_args_def:
            name = wrapper_arg['name']
            try:
                argval = wrapper_arg_vals.pop(0)
            except IndexError:
                if name in kwargs:
                    wrapper_kwargs[name] = kwargs[name]
                    del kwargs[name]
                elif 'default' in wrapper_arg:
                    wrapper_kwargs[name] = wrapper_arg['default']
                else:
                    raise TypeError("%s() missing keyword argument '%s'" % (wrapped.__name__, name))
            else:
                if name in kwargs:
                    raise TypeError("%s() got an unexpected keyword argument '%s'" % (wrapped.__name__, name))
                wrapper_kwargs[name] = argval
        else:
            #check whether any superflouos arguments were given
            if wrapper_arg_vals:
                expected_len = len(wrapper_args_def) + wrapped_argslen
                raise TypeError("%s() and decorator altogether take at most %d argument(s) (%d given)"
                                        % (
                                                wrapped.__name__,
                                                expected_len, 
                                                len(args), 
                                            )
                                    )
    
    #return the wrapper arguments and the remaining args and kwargs for wrapped
    return funcargs, kwargs, wrapper_kwargs


def _add_pattern_arguments(wrapped=None, wrapper_args_def=None):
    """Outer wrapper receiving the arguments for the wrapper
    
    This function is called when ``_add_pattern_arguments`` decorator is applied
    to a wrapped function either with or without arguments.
    
    When applied without arguments (and no brackets), ``wrapped`` is set to the
    wrapped function object and no ``wrapper_args_def``.
    
    If applied as ``@_add_pattern_arguments(wrapper_args_def=<>)``, no wrapped
    function object is given, only the ``wrapper_args_def``. In this case we
    record the ``wrapper_args_def`` and use functools to create partial object,
    which will be the replacement of the wrapped function.
    
    Args:
        wrapped (function object): the decorated function
        wrapper_args_def tuple): definition of list of arguments which are used by
            the wrapper only. Each such argument is defined by a dict with keys of
            ``name`` and ``default``.
    
    Note:
        @_add_pattern_arguments should use keyword arguments to be unambigous,
        as we have to figure out whether we were given the wrapped function or not.
        Well, if positional arguments are used and the first argument is not callable
        (i.e. not a function object (but the ``wrapper_args_def`` tuple), it is recognized.
    
    Returns:
        function object: the replacement (decorated) function
    """
    #when this function is called like @decorator_name(<arguments>). no wrapped function is given
    if not callable(wrapped):
        #create partial object, which will be the replacement of the wrapped function
        return functools.partial(_add_pattern_arguments, wrapper_args_def=wrapper_args_def)
    
    #get the wrapped function args length (minus the self, if any)
    #this has to suppose that the instance variable is called 'self', because
    #for some reason wrapped is a function here, not a method and
    #inspect.ismethod(wrapped) returns False :-(
    argslist = inspect.getargspec(wrapped).args
    wrapped_argslen = len(argslist)
    if argslist and argslist[0]=='self':
        wrapped_argslen -= 1
    
    @decorator
    def wrapper(wrapped, self, args, kwargs):
        """The decorator function that replaces the wrapped func
        
        It is to extract the patterns from the arguments and compile them if needed.
        Then call the reading function with the reduced arguments.
        
        Args:
            wrapped (function object): the decoreated reading function
            self (obj): the nbsr instance
            args: the positional arguments tuple for the decorated function
            kwargs: the keyword arguments dict for the decorated function
        
        Returns:
            any: whatever the reading function is to return
        """
        #first check whether queue exists at all, where we want to read data from
        if self.linequeue is None:
            raise ReadException('Cannot read before NBSR worker start')
        
        #extract the arguments of the wrapper from all the arguments
        args, kwargs, wrapper_kwargs = _separate_args(
            wrapped,
            wrapped_argslen,
            wrapper_args_def,
            args, kwargs
        )
        
        #compile the patterns
        self._compile_patterns(**wrapper_kwargs)
        
        #call the wrapped reading function with the remaining arguments (self is sent by decorator)
        return wrapped(*args, **kwargs)
    
    return wrapper(wrapped)


class Mixin(object):
    """Mixin class for NonBlockingStreamReader, providing private methods"""
    #####
    ## class variables set dependent on Python 2 or 3
    #####
    #What type do we consider a pure pattern text (in contrast with compiled pattern)? Python 2: str & unicode; Python 3: str & bytes
    puretextpattern = (str, bytes) if sys.version_info[0]>2 else (str, unicode)
    #What class do we consider an re compiled pattern? From Python 3.7: re.Pattern; otherwise re._pattern_type
    re_pattern = re.Pattern if sys.version_info[0]>2 and sys.version_info[1]>6 else re._pattern_type
    #What ?????????
    
    def _populate_queue(self, stream):
        '''In a separate thread, read data from 'stream' and put them in the 'queue'
        
        Worker function to be run as a child thread. It only reads 1 character at a time
        and put it into the queue. As long as there is no more character to read, but there
        is no EOF yet (i.e. when the stream source is a bit stuck), this thread hangs.
        Reading only 1 character makes sure all data is read from the stream before
        it hangs. 
        
        Child thread cannot and must not raise exception, so if such is needed the 
        exception instance is put into the queue, and the queue consumer is responsible
        to notice this and raise the exception in the main thread.
        
        This method only returns (and the thread terminates) when
        
            - EOF is reached on the stream
            - the self.worker_allowed is found False at the beginning of a read cycle
            - exception occurs
        
        Writing the self.EOF is thread-safe, as this is the only place it is written, i.e. the
        main thread only reads it.
        
        Args:
            stream (stream): the open stream where we read from
        '''
        #loop on reading lines
        while True:
            #worker not needed anymore?
            if not self.worker_allowed:
                return
            
            try:
                #read 1 byte (type: str or bytes) and block until this byte can be read or stream gets closed
                queue_elem = stream.read(1)
                
            except ValueError as e:
                #catch the exception when the stream became unexpectedly closed
                if stream.closed:
                    queue_elem = StreamUnexpectedlyClosed(repr(e))
                else:
                    #well, catch other ValueError exceptions too, even if we do not expect such
                    queue_elem = e
            except Exception as e:
                #put any non-terminating exception instance on the queue, even if we have no idea what they are
                queue_elem = e
            
            #put the character/byte (or empty string/bytes, if EOF), or exception instance into the queue
            self.linequeue.put(queue_elem)
            
            #standard I/O read returns empty string/bytes on EOF
            if not queue_elem:
                #set the EOF flag
                self.EOF = True
                #finish the worker on EOF
                return
    
    
    def _readone(self, timeout=None):
        """Private function to read one character from the stream
        
        It is the consumer of the queue.
        
        If there is stream data in the queue or appears stream data in the alotted
        timeout, this functon returns a char.
        On EOF, it returns an empty string immediately (same behaviour as regular read).
        Otherwise, it raises the private _TimeOutOccured exception.
        
        The timeout can be explicitly provided in the argument or it is taken from the
        preset. 
        
        Args:
            timeout (optional float): the timeout the reading max wait if the queue
                is empty. If missing or None, the atomic_timeout set earlier (in init or
                set_timeout) is used.
        
        Returns:
            str or bytes: 1 character/byte from the stream, or empty string/bytes on
                timeout or EOF
        
        Raises:
            _TimeOutOccured: no character arrived from the stream in the alotted time
            StreamUnexpectedlyClosed: the stream got closed while we were reading it
        """
        try:
            #get an element from the queue. Use the explicit timeout if exists, otherwise atomic
            queueelement = self.linequeue.get(
                block=True,
                timeout=timeout or self.atomic_timeout
            )
        
        #no data in the queue?
        except queue.Empty:
            #EOF already?
            if self.EOF:
                #there is no worker to populate the queue anymore, so just say EOF again
                return self.empty_str_or_bytes
            else:
                #raise exception
                raise _TimeOutOccured
        
        #if there was an error in the worker thread, it did put an instance of a descendant class of Exception into the queue
        if isinstance(queueelement, Exception):
            #raise the exception that the worker indicated
            raise queueelement
        
        #if str, bytes or unicode was taken from the queue, just return it
        else:
            if self.debugprint:
                print(queueelement, end='', flush=True)
            return queueelement
    
    
    def _readbunch(self, size, newlinecheck=False):
        """Private function to read a bunch of data from the stream defined at
        instance creation
        
        It tries to read as many data as possible until EOF, an end condition,
        or (on timeout) a matched pattern. An end condition can be the required
        number of bytes read for read(), or a new line caracter for readline(). It
        then returns whatever it could read.
        
        If reading ends for more than one reasons (i.e. pattern would match but
        there is EOF too), the precedence for returned reason is EOF first, then
        end condition and then pattern match. I.e. patterns are only checked
        (and pattern_index and match_object set), if there was some timeout and
        there is no other reason for finishing reading.
        However, if pattern check is still needed, do_pattern_check() can be used.
        
        If the return reason is a pattern match, the instance attributes of
        pattern_index and match_object are set (otherwise they are None).
        
        Args:
            size (int): the max amount of data (number of bytes) to be read
            newlinecheck (optional bool): whether a newline is to stop this bunch
                reading
        
        Returns:
            str or bytes: the read data if any, or empty string. Note that the return string
                does not indicate whether there was EOF or timeout. Such info can
                be retried from the returnby attribute.
        
        Raises:
            StreamUnexpectedlyClosed: the stream got closed while we were reading it
            or any exception that might have occured in the worker thread
        """
        #we are going to collect characters in the buffer (bytes or str, dependent on stream mode)
        buffer = self.empty_str_or_bytes
        
        #0 byte was requested? Does it make any sense? Anyway...
        if size == 0:
            return buffer
            
        #first try to get the character from the buffer
        try:
            buffer += self.bufferedchars.pop(0)
            cnt = 1
            #only 1 byte was requested?
            if size == 1:
                return buffer
        except IndexError:
            cnt = 0
        
        #indicate that no any pattern matched yet
        self.pattern_index = None
        self.match_object = None
        
        #the next timeout, whether atomic_timeout is to be used or long wait (None=atomic)
        this_timeout = None
        
        #loop on reading characters until an end condition or EOF is found, or timeout
        while True:
            try:
                #read 1 character with atomic_timeout for 1st read, or timeout after that
                ch = self._readone(this_timeout)
            
            except _TimeOutOccured:
                #this_timeout=None indicate that this was an atomic timeout
                if this_timeout is None:
                    #progress to pattern search (after the else clause)
                    pass
                else:
                    #if long timeout occured, return the content of the buffer (can be empty)
                    self.returnby = returnby_TIMEOUT
                    return buffer
            
            except Exception:
                #if the stream became closed, or any other exception, let the exception escalate to the caller
                raise
            
            #successful read
            else:
                #no character read?
                if not ch:
                    #return the buffer at EOF (NB, no pattern check even if it would match)
                    self.returnby = returnby_EOF 
                    return buffer
                
                #add the character to the buffer and increase counter
                buffer += ch
                cnt += 1
                
                #size limit reached? NB, it will never match to -1 (unlimited)
                if cnt == size:
                    #we have read enough, return the buffer
                    self.returnby = returnby_SIZE
                    return buffer
                
                #newline char is to be searched for readline() and readlines()
                if newlinecheck:
                    if ch == self.newline_char_or_byte:
                        #if it is at the end of a line, return the line (can be an empty line)
                        self.returnby = returnby_NEWLINE
                        return buffer
                
                #the previous read might have had long timeout, so reset it now to atomic timeout after a successful read
                this_timeout = None
                
                #read on
                continue
                
            #as atomic timeout happened, check patterns whether any of them matches
            if self.is_patternmatch(buffer):
                #set the return reason and return the buffer
                self.returnby = returnby_PATTERN
                return buffer
            
            #set a longer timeout for the next read and continue reading attempt
            this_timeout = self.timeout_diff
            continue
        
    
    def _compile_patterns(self, expected_patterns=None, regexflags=0):
        """Private function for compiling re patterns
        
        Reading functions can receive a list of expected patterns. If low level reading
        experiences (an atomic) timeout, it checks whether one of these patterns
        match, and if so, it does not wait longer but returns to the caller.
        
        Elements in this received list may not be compiled yet. The wrapper of the
        reading functions calls this method, which will compile those ones that are
        text patterns, using the optional re flags.
        
        Args:
            expected_patterns (optional tuple/list): a list of patterns that we wait for.
                If any of these patterns match, we return immediately, not waiting
                for EOF or timeout. List elements (the patterns) can be pure text or
                re compiled. If this argument is missing or set to None, reading functions
                keep using the previous pattern list, if any. An explicit empty list will
                however remove previous list and reading functions do not check for
                any patterns from then on.
            regexflags (optional int): see the re module, e.g. re.IGNORECASE. Or
                re.VERBOSE meaning white space is not part of the pattern (unless
                escaped) and comments can appear. Note that if expected_patterns
                element is already compiled, these flags here are ignored.
        
        Raises:
            rePatternError: One of the expected patterns cannot compile
        """
        #no new patterns are defined
        if expected_patterns is None:
            #just keep whatever existing compiled patterns we have
            return
        
        #reset and collect compiled patterns
        self.compiled_patterns = []
        
        #sanity check of the expected pattern list
        if not isinstance(expected_patterns, (list, tuple)):
            raise ValueError(
                'expected_patterns should be either a list or tuple, '
                'but it is %s'%type(expected_patterns)
            )
        
        #loop on all received pattern, if any
        for expected_pattern in expected_patterns:
            #already compiled?
            if isinstance(expected_pattern, self.re_pattern):
                #figure out they type of the pattern that was compiled
                pattern_type_binary = isinstance(expected_pattern.pattern, bytes)
                
                #indicate that the pattern is already compiled
                alreadycompiled = True
            
            #pure text pattern (text can be bytes too)?
            elif isinstance(expected_pattern, self.puretextpattern):
                #figure out they type of the pattern
                pattern_type_binary = isinstance(expected_pattern, bytes)
                
                #indicate that the pattern is already compiled
                alreadycompiled = False
            
            #unrecognised pattern type?
            else:
                raise ValueError(
                    'The expected pattern %s can only be a string/bytes, '
                    'or an already compiled re pattern, '
                    'but %s found'%(repr(expected_pattern), type(expected_pattern))
                )
            
            #XOR the stream and the pattern type (yields True when they do not match)
            if self.is_binarystream ^ pattern_type_binary:
                if self.is_binarystream:
                    raise ValueError(
                        'A binary stream cannot be searched for with a non-binary pattern '
                        '%s'%(repr(expected_pattern))
                    )
                else:
                    raise ValueError(
                        'A non-binary (text) stream cannot be searched for with a binary pattern '
                        '%s'%(repr(expected_pattern))
                    )
            
            if alreadycompiled:
                #just append the compiled re pattern into the list
                self.compiled_patterns.append(expected_pattern)
                
            else:
                try:
                    #compile the pattern and append it to the list
                    self.compiled_patterns.append(
                        re.compile(
                            expected_pattern,
                            regexflags
                        )
                    )
                
                except Exception as e:
                    raise rePatternError(
                        'compile error in pattern %s:%s'%(
                            repr(expected_pattern),
                            str(e)
                        )
                    )
