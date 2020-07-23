"""This is the main module of the Non-blocking Stream Reader package

The package contains other modules providing private methods, etc. but they are
not important for a user. If you are really into it, see the source code.
"""


import io
import threading
import queue
from .exceptions import NonStreamException, _TimeOutOccured
from .returnbys import returnby_NEWLINE
from . import privates
from .returnbys import *


class NonBlockingStreamReader(privates.Mixin):
    """Class to define a stream reader that can have timeout and does not block
    
    The standard I/O actions are blocking. E.g. readline() does not return until it reads
    a newline character or reaches EOF. Or, a read(4096) won't return until all 4KB is
    read or EOF reached. If the process feeding the stream gets stuck (e.g. waiting for
    an answer/password), i.e. it does not produce enough data and do not terminate
    either, the regular I/O read will hang.
    
    Obviously no blocking happens when the source is e.g. a local file. This
    package is to support those who read a stream via a slow, unreliable stream.
    E.g. a remote telecom network element can be such. We may want to
    communicate with such over e.g. SSH. We build a pipe and read data from the
    network element on its STDOUT or STDERR. Such communication usually needs
    interaction, too.
    
    NBSR stands in between the original stream and the reader function of the caller.
    This class takes an output stream and provides a replacement output stream with
    the same read methods. It creates a working thread that keeps reading the original
    output stream (which may get stuck) and puts the stream content into a gueue.
    While the main thread reads the queue and handles timeout, it also recognises
    patterns in the stream content.
    
    The original stream remains accessible to the caller, i.e. the caller may read the
    original stream parallel with the NBSR stream, but it can lead to total chaos.
    
    Reading the NBSR stream will obviously be slower, as the standard I/O reads the
    stream in chunks, not byte-by-byte, and does not do pattern matches either.
    However, when the stream source is slow anyway and pretty unreliable (jittery),
    the speed is not an issue.
    
    The original stream can be provided at init, which will then automatically creates
    the working thread and starts reading the stream. Alternarively, the instance can
    be created without a stream and the start_worker() method is called explicitly with
    a stream later.
    
    Reading attempt from the NBSR stream raises exception before the worker is started.
    
    The working thread can be stopped if the caller wishes to continue the reading
    directly from the original stream. This may happen when the caller is sure that
    the stream will produce enough data for the standard I/O read methods, and wish to
    speed up the reading. Or in case no any further reading is needed. If so, the caller
    can call stop_worker() method. Reading functions are still available after the worker
    is stopped, or even after the original stream is closed, because there are still data
    in the queue. If the caller wants to continue reading the original stream, it needs
    to read off all the data from the queue first. When the queue goes empty, the last
    read will return due to timeout. The caller may want to reduce the timeout value
    with calling set_timeout() method before calling the read methods when emptying
    the queue, to reduce the timeout waiting at the end.
    
    Timeouts:    
        This class provides the timeout feature, to overcome the issue of hanging I/O
        actions. Actually, 2 kinds of timeouts can be defined:
        
        - Atomic timeout
            It is how much we wait for a single data on the stream. If this timeout
            happens, the bunch of the read data is tested to a list of patterns. I.e. we
            may be waiting for a prompt or a ``-- more --`` line. If any of the patterns
            is matched, the reading function returns with the read data. The index of the
            matched pattern can be retrieved (and can be handled by the caller). The
            pattern may contain capturing groups. Such captured groups can be
            retrieved from the re.Match object.
        - Timeout
            If atomic timeout happened and none of the patterns matched, further
            read is attempted with a lot longer timeout. Typically atomic
            timeout is a fraction of a second while a normal timeout is several
            seconds.
        
        This timeout algorithm provides a fairly fast reaction capability to
        given situations, like a prompt, but allow the slow remote network
        element long dormant periods.
    
    Algorithm of this package:
        It creates a queue, which is fed by a thread using the standard I/O read(1). The
        main process gets the data from the queue and checks whether enough data
        arrived, e.g. a readline() will only take data from the queue until a new line or an
        EOF occurs. If the stream producer (e.g. remote network element) stops sending
        data, the standard I/O read in the thread gets blocked, the queue runs empty if
        the main process take all the data. After a timeout, the main process returns all
        the read data to the caller. The caller can obtain the reason of returning by calling
        the extra methods below.
        
        If the stream producer still does not provide data (the queue is still empty), any
        sub-sequent calls of NBSR reading function will result in returning empty string after
        the timeout. The return-by reason gets updated.
        
        It is the caller's responsibility to feed response to the stream producer or terminate
        it, so that stream reader worker thread unblocks and/or terminates.
    
    Reading methods:
        This class provides the following read methods, which provide the same functionality
        as their similarly named standard I/O functions, but of course with the timeout feature.
        They return the data read from the stream and they always return at the latest
        specified by the timeout:
        
        - :func:`read()`
        - :func:`readline()`
        - :func:`readlines()`
        
        The reading methods above can also receive the following _`parameters`:
        
        - expected_patterns (optional tuple/list): a list of patterns that we wait for.
            If any of these patterns match, we return immediately, not waiting
            for EOF or normal timeout. List elements (the patterns) can be pure text or
            re compiled.
        - regexflags (optional int): see the re module, e.g. re.IGNORECASE. Or
            re.VERBOSE meaning white space is not part of the pattern (unless
            escaped) and comments can appear. Note that these flags are ignored,
            where the element of the expected_patterns list is already compiled.
            By default, none of the flags is set, i.e. 0.
        
    Additional methods:
        Reading functions only return the data read (or empty string), as their standard
        counterparts would do. I.e. you cannot tell from a returned empty or any truncated
        string whether there was EOF or timeout. Any such info, i.e. whether it is EOF or
        what pattern matched (if any), has to be retrieved by the caller separately. Caller can
        optimize the interaction with dynamically setting timeouts. See the extra methods
        below:
        
        - :func:`start_worker()` can be used to start the worker thread that reads the stream,
            in case the stream was not provided at init.
        - :func:`stop_worker()` can be used to stop the worker thread that reads the stream.
            Note that the queue may contain already read data, which cannot be put back on
            the original stream, so the needs to read up the content of the queue, before reading
            the original stream outside of NBSR.
        - :func:`set_timeout()` is to set/change the timeout values for subsequent reading
        - :func:`found_pattern_info()` is to retrieve the info of the pattern if it was matched
        - :func:`is_sending()` is to test whether the stream is sending data (yet), i.e. any data can
            be read from the stream. This can be used in the begining of reading the stream
            as the wait time (timeout) can be a lot longer than the timeout between subsequent
            reading.
        - :func:`return_reason()` provides the reason why the last reading function returned
        - :func:`is_patternmatch()` is to force a pattern check in case the return reason was some
            higher priority reason, like EOF
        - :func:`is_EOF()` can be used to check whether EOF has reached. As the reading functions
            simply return empty string if we call them after EOF is reached, checking EOF could
            be useful.
        - :func:`close()` does not actually close any stream. It only calls stop_worker(0.5).
            Calling close() subsequently does not cause any exception, similar to the standard
            I/O close. It is the caller's responsibility to get the original stream closed, e.g. by
            calling the terminate() method of the pipe.
    
    Example:
        A typical use is to open a pipe, read the output of the pipe, figure out whether a pattern
        matched, send answer/input to the stdin of the pipe, handle the next interaction, etc.
        A working example can be found in the package, see `testexec.py`. It uses a `feeder.py`
        remote process and the `test.py` reading process. The skeleton of a typical flow is as
        below::
        
            pipe = subprocess.Popen(...) #see package 'subprocess'
            
            #create the NBSR stream; timeout for the dialogue is set to 3.5 seconds
            with nbsr.NonBlockingStreamReader(pipe.stdout, timeout=3.5) as nb_stdout:
            
                # wait up to 15 seconds for the remote to boot and start sending data
                if not nb_stdout.is_sending(15):
                    raise <Remote cannot set up in a fairly long time>
                
                linebuffer = []
                for line in nb_stdout.readline(expected_patterns=['prompt>']):
                    linebuffer.append(line)
                
                    #if prompt pattern (index=0) was found, send the command
                    if nb_stdout.found_pattern_info()[0] == 0:
                        pipe.stdin.write('ls -l\n')
                        break
                
                #read the command output lines until the next prompt or error (index=1)
                linebuffer += nb_stdout.readlines(expected_patterns=['prompt>', 'error'])
                if nb_stdout.found_pattern_info()[0] == 1:
                    raise <there was an error>
                
                #send the kill command, so that the remote output stream goes EOF
                pipe.stdin.write('exit\n')
            
            #close the pipe
            pipe.terminate()
        
    Important:
        Our worker thread keeps reading the stream until EOF. Unfortunately, we cannot
        kill the worker thread from the main thread in Python, so the only way to get the
        worker thread terminate is closing the stream in the remote process.
        
        Well, :func:`stop_worker()` method tries to stop the worker thread, but it is only
        possible when its get() is not blocked, i.e. there are still data on the stream.
        
        Normally, terminating the pipe kills the remote process and EOF happens. However,
        when the remote process is launched in a shell, this does not always seem to
        happen. Not sure why.
    
    Args:
        stream (optional stream): an open stream where we read data from. This is
            usually a STDOUT (or STDERR) of a piped process. The stream can be given
            later, like explicitly calling the :func:`start_worker()` method.
        timeout (optional float, int or None): the reading timeout in seconds. By default
            it is None, meaning return is immediate, even if there is no data on the stream.
            See also :func:`set_timeout()`.
        atomic_timeout (optional float): the timeout before pattern match check is done
            on the data read from the stream. By default it is 1/100 sseconds.
            See also :func:`set_timeout()`.
        debugprint (optional bool): Leave it the default False, it is for development only.
            This is planned to be converted to a correct logging function in the future.
    
    Raises:
        NBSRbaseException: base exception, not raised ever, all errors are sub-classes
        NonStreamException: the provided object in 'stream' is not of a stream type
        StreamUnexpectedlyClosed: the stream got closed while we were reading it
        WorkerRunningException: attempt to start the worker thread more than once
        ReadException: any reading attempt is made before starting the worker
        rePatternError: One of the expected patterns cannot compile
        ValueError: raised when timout agruments do not make sense
    """
    #default wrapper arguments for reading functions
    PATTERN_ARGS = (
        dict(
            name='expected_patterns', 
            default=None,
        ), 
        dict(
            name='regexflags', 
            default=0,
        ), 
    )
    
    def __init__(self,
        stream=None,
        timeout=None,
        atomic_timeout=0.01,
        debugprint=False
    ):
        #check whether the timeouts are of the correct type
        if not isinstance(timeout, (float, int, type(None))):
            raise ValueError(
                'Received {} timeout, but float, '
                'int or None was expected'.format(type(timeout))
            )
        if not isinstance(atomic_timeout, (int, float)):
            raise ValueError(
                'Received {} atomic timeout, '
                'but int/float was expected'.format(type(atomic_timeout))
            )
        
        #timeout: the timeout in seconds or fractions of seconds that we wait until
        #  the read function returns, in case the required amount of data or the
        #  required type of data has not been received yet. None means immediate
        #  return
        #atomic_timeout (float): the timeout for reading 1 byte from the stream
        #timeout_diff (float): it is the difference of how much the timeout is longer
        #  than the atomic_timeout
        self.set_timeout(timeout, atomic_timeout)
        
        #store the flag whether debug printing is needed
        self.debugprint = debugprint
        
        #set the EOF flag to false by default
        #EOF (bool): flag indicating whether the stream reached EOF and the worker
        #  thread already finished/returned, i.e. nothing more can be read from the stream
        self.EOF = False
        
        #the collected compiled patterns for reading functions
        self.compiled_patterns = []
        
        #pattern_index (int): the index of the found pattern. If no pattern was found (yet),
        #  it is None.
        #match_object (re.MatchObject): the match object returned by the ``re`` search
        self.pattern_index = None
        self.match_object = None
        
        #returnby (int): enum value indicating the reason of the last read function,
        #  See module returnbys.py
        #  By default indicate that no any return reason is available yet
        self.returnby = returnby_UNDEF
        
        #bufferedchars (list): a buffer which is filled during is_sending() and emptied by the _readone()
        self.bufferedchars = []
        
        #when the worker is started it will be a threading.Thread instance
        self.workerthread = None
        #starting the worker will create a queue.Queue()
        self.linequeue = None
        
        #stream was given?
        if stream is not None:
            #check the stream as it has to be open
            if stream.closed:
                #simulate a standard reading function reaction on an attempt of reading a closed stream
                raise ValueError('I/O operation on closed file')
            
            #start the worker right away
            self.start_worker(stream)
    
    
    def __enter__(self):
        #init and start must have done everything, so this enter is a dummy
        return self
    
    
    def __exit__(self, type, value, traceback):
        #close whatever can be closed
        self.close()
        #return False to indicate that no exception is to be swallowed
        return False
    
    
    def start_worker(self, stream):
        """Start the worker thread that reads the stream
        
        Args:
            stream (stream): an open stream where we read data from. This is usually
                a STDOUT (or STDERR) of a piped process.
        """
        #do not allow start multiple times
        if self.workerthread:
            raise WorkerRunningException('Worker thread already started')
        
        #check whether a stream-type object has arrived in 'stream'
        if not isinstance(stream, io.IOBase):
            raise NonStreamException(
                'Received {} instead of a file type'.format(type(stream))
            )
        
        #figure out the stream mode
        if hasattr(stream, 'mode'):
            self.is_binarystream = 'b' in stream.mode
        else:
            self.is_binarystream = not isinstance(stream, io.TextIOWrapper)
        
        #create values dependent on whether binary or text
        self.empty_str_or_bytes = b'' if self.is_binarystream else ''
        self.newline_char_or_byte = b'\n' if self.is_binarystream else '\n'
        
        #linequeue (queue.Queue): the queue where we put the read data
        self.linequeue = queue.SimpleQueue()
        
        #create a worker thread instance
        self.workerthread = threading.Thread(
            target=self._populate_queue,
            args=(stream, )
        )
        
        #indicate that worker is allowed to run
        self.worker_allowed = True
        
        #start the worker thread as a non-daemon
        self.workerthread.daemon = False
        self.workerthread.start()
    
    
    def stop_worker(self, timeout=None):
        """Stop the worker thread and wait until it terminates
        
        Since we cannot kill a thread only ask it to die, this method sets the flag that
        makes the worker thread terminate (when it is not blocked). This method waits
        until the worker thread stopped then reads the queue and returns it.
        
        NB, the worker thread won't terminate if it is waiting for the stream. If no
        'timeout' is set, this method will hang.
        
        If 'timeout' is set, this method returns, but the worker thread will still hang there
        and, if a char appears on the stream, it will read it off. This situation is indicated
        in the return value.
        
        Args:
            timeout (float): the number of seconds we wait for the worker thread to
                terminate, before returning to the caller
        
        Returns:
            bool: whether the worker thread stopped successfully (or it was not active anyway)
        """
        #no running worker?
        if not self.workerthread:
            #imitate successful thread termination
            return True
        
        #set the flag
        self.worker_allowed = False
        
        #wait for the worker to terminate
        self.workerthread.join(timeout)
        
        #thread still alive, i.e. there was a timeout in join?
        if self.workerthread.is_alive():
            #state that the worker thread remained live because it is blocked
            return False
        else:
            #forget the thread instance
            self.workerthread = None
            #state that the worker thread successfully stopped
            return True
    
    
    @privates._add_pattern_arguments(wrapper_args_def=PATTERN_ARGS)
    def read(self, size=-1):
        """Read as many as size characters from the stream
        
        This method never blocks. 
        
        If the required amount of characters can be read within the timeout, it behaves as
        a regular read(). If some data is read but not enough until the timeout, the so-far
        read data is returned. If there are no more data and the stream is stuck or
        EOF, it returns empty string (exactly as the standard read() would do on EOF).
        
        Args:
            size (optional int): the max amount of data (number of bytes) to be read.
                By default, -1, meaning no limit.
        
        See additional parameters_.
        
        Returns:
            str or bytes: maximum size bytes or whatever could be read. On EOF, an empty
            string is returned.
        
        Raises:
            StreamUnexpectedlyClosed: the stream got closed while we were reading it
                or any exception that might have occured in the worker thread
        """
        #read a bunch of data, and indicate no stop character
        return self._readbunch(size=size)
    
    
    @privates._add_pattern_arguments(wrapper_args_def=PATTERN_ARGS)
    def readline(self, size=-1):
        """Read one line (or part of it) from the stream
        
        This method never blocks. 
        
        If the line can be read within the timeout, it behaves as a regular readline().
        If some data is read but no newline arrives until the timeout, the so-far
        read data is returned. If there are no more data and the stream is stuck or
        EOF, it returns empty string (exactly as regular readline would do on EOF).
        
        Args:
            size (optional int): the max amount of data (number of bytes) to be read.
                By default, -1, meaning no limit.
        
        See additional parameters_.
        
        Returns:
            str or bytes: a full line, part of a line, i.e. whatever could be read. On EOF, an
            empty string is returned.
        
        Raises:
            StreamUnexpectedlyClosed: the stream got closed while we were reading it
                or any exception that might have occured in the worker thread
        """
        #read a bunch of data, and indicate whether reading should stop on newline
        return self._readbunch(size=size, newlinecheck=True)
    
    
    @privates._add_pattern_arguments(wrapper_args_def=PATTERN_ARGS)
    def readlines(self):
        """Read all lines (or as many as possible) from the stream
        
        This method never blocks. See the details under readline().
        The standard I/O readlines() has a hint argument, but it is not implemented
        in NBSR due to performance reasons.
        
        See additional parameters_.
        
        Returns:
            list: the list of the lines read. Lines are terminated by newline, except the last
                line which may or may not have a newline at the end.
                On EOF, an empty list is returned.
        
        Raises:
            StreamUnexpectedlyClosed: the stream got closed while we were reading it
                or any exception that might have occured in the worker thread
        """
        #we are going to collect lines in a list
        lines = []
        
        #loop on reading lines as long as the previous reading returned with newline
        while True:
            #read 1 line string
            line = self.readline(self.compiled_patterns)
            
            #add the line to the list. NB, lines+=line would add each char in the line as a separate list element
            lines.append(line)
            
            #only break from the loop is the last return-by was not a newline (i.e. EOF, PATTERN, etc.)
            if self.returnby != returnby_NEWLINE:
                break
            
        #return all the lines whatever was read
        return lines
    
    
    def set_timeout(self, timeout, atomic_timeout=None):
        """Set the timeout for the sebsequent read actions
        
        Args:
            timeout (float, int or None): the timeout the reading max wait if the queue is empty
            atomic_timeout (optional float): the timeout for reading 1 byte from the stream.
                If not given (or None) the atomic_timeout provided in init is not changed.
        
        Raises:
            ValueError if timout agruments do not make sense
        """
        #store the received timeout
        if not isinstance(timeout, (float, int, type(None))):
            raise ValueError('timeout should be a float, int or None, but it is %s' % str(type(timeout)))
        if timeout <= 0:
            raise ValueError('timeout (%s) should be a positive value' % str(timeout))
        self.timeout = timeout
        
        #store the received atomic_timeout
        if atomic_timeout is not None:
            if not isinstance(atomic_timeout, float):
                raise ValueError('atomic_timeout should be a float, but it is %s' % str(type(atomic_timeout)))
            if atomic_timeout <= 0:
                raise ValueError('atomic_timeout (%s) should be a positive value' % str(atomic_timeout))
            self.atomic_timeout = atomic_timeout
        
        #if timeout is not None, check that it is bigger than atomic timeout
        if self.timeout is not None:
            #check that values make sense
            if self.atomic_timeout > self.timeout:
                raise ValueError(
                    'atomic_timeout (%s) should not be bigger than timeout (%s)' % (str(self.atomic_timeout), str(self.timeout))
                )
                
        #calculate the difference and store it as an integer
        if self.timeout is not None:
            self.timeout_diff = self.timeout - self.atomic_timeout
        else:
            self.timeout_diff = 0
    
    
    def found_pattern_info(self):
        """Get the info of the found pattern
        
        Returns:
            tuple: the index of the found pattern and its match object, i.e.:
                
                int: the integer index of the found pattern. If no pattern was found, it is None
                
                re.MatchObject: the match object containing captured sections in the pattern.
                If no pattern was found, the value of this object is undefined, so check the
                index first.
        """
        return self.pattern_index, self.match_object
    
    
    def is_sending(self, timeout):
        """Test the stream by reading 1 character
        
        This method can be used immediately after opening the stream and waiting for the
        remote process to start up and start sending.
        
        The method waits up to the timeout and indicates whether the remote process is
        sending (or started to send) data on the stream. We test the stream by trying to
        read 1 character. This character cannot be pushed back to the stream, so it is
        buffered and the next reading function will contain it (along with other read
        characters).
        
        Args:
            timeout (float or int): the timeout the reading max wait if the queue is empty
                This timeout value is only temporary for this test and does not affect the
                timeout set in the init or set_timeout(), i.e. independent from other reading
                timouts.
        
        Returns:
            bool: whether a character can be read from the stream
        
        Raises:
            StreamUnexpectedlyClosed
        """
        #try to read a character from the stream (or buffer)
        try:
            char = self._readone(timeout)
        
        #only catch the timeout, let all other exections (like StreamUnexpectedlyClosed or any OSError escalate)
        except _TimeOutOccured:
            #indicate that the stream is not sending data (i.e. still booting up or stuck or EOF)
            return False
        
        #store the read character in the buffer (LIFO)
        self.bufferedchars.append(char)
        
        #indicate that the stream is sending data
        return True
    
    
    def return_reason(self):
        """Provide the reason why the last reading function returned
        
        Returns:
            int: one of the returnby_xx constants, where xx can be:
            
                - EOF
                - SIZE
                - NEWLINE
                - PATTERN
                - TIMEOUT
            
            Negative value (returnby_UNDEF) means that no reading method
            has been called yet.
            
            Note that multiple conditions can occure at the same time, i.e.
            size is reached as well as EOF occurs, or new line has been read
            and pattern would match too. In such cases only 1 reason is set
            and EOF has the highest priority, then SIZE, then NEWLINE, then
            PATTERN, and at last TIMEOUT.
            This precedence is reflected in the assigned values, i.e.
            returnby_EOF < returnby_SIZE < returnby_NEWLINE < returnby_PATTERN ...
            
            Also note that the found pattern info is only set if the return reason
            is pattern. Therefore, the caller can force a pattern matching by
            calling is_patternmatch().
        """
        return self.returnby
    
    
    def is_patternmatch(self, input):
        """Do a pattern check on the input with the set of last used patterns
        
        This method sets/resets the matched pattern info returned by 
        
        Args:
            input (str): an arbitrary string to be checked against the patterns
        
        Returns:
            bool: whether any patter in the list matched the input
        """
        #loop on expected patterns whether any of them matches
        for idx, compiled_pattern in enumerate(self.compiled_patterns):
            matchObj = compiled_pattern.match(input)
            if matchObj:
                #set the pattern order number so that it can be read by the caller
                self.pattern_index = idx
                #save the match object so that the caller can get it
                self.match_object = matchObj
                #indicate match to the caller
                return True
        
        #if the loop exhausted, indicate no match
        self.pattern_index = None
        self.match_object = None
        return False
    
    
    def is_EOF(self):
        """Test whether EOF has reached
        
        Returns:
            bool: flag whether EOF has reached
        
        Note:
            This function purely indicates whether we reached EOF with reading the stream
            with nbsr read methods. So, if we did not read until EOF, or read the stream
            to EOF with other functions than this nbsr instance, or even if the stream
            got closed, this function still returns False, as if the stream could still be read.
            
            Also, this EOF check works without exception even after the stream
            has been closed.
        """
        return self.EOF
    
    
    def close(self):
        """Actually not closing any stream, but sort of trying to tidy up
        
        Killing the worker thread would be nice but not possibe. Instead, we ask the worker
        thread to stop. Whether it really stops in half a second or not, we do not care in
        this method. Should the caller be curious to know the status of the worker thread,
        it can call the stop_worker() repeatedly and check the returned status, or make
        sure the stream feeder process stops and the stream is closed (that would then
        cause the worker thread stop).
        """
        #try to stop the worker thread and wait max half a second, then ignore whether it was successful
        self.stop_worker(timeout=0.5)
