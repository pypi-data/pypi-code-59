# This is the file which I use to run most of the tests
# Although some tests use custom functions, most of them
# use this

import time
import traceback

# For colored output
import colorama

# Initiate the colored output
colorama.init()

# This variable stores the number of tests
global test_count
test_count = 0

# The base class for the tests
class TestSuite:
    def __init__(self, **info):
        global test_count

        test_count += 1 # Increase the nmber of tests done by one
        details = {'name': test_count, 'tests': [], 'setup': None, 'cleanup': None} # Let us assume a base template
        details.update(info) # Update it with the arguments provided

        # Save the details
        self.name = details['name'] 
        self.tests = details['tests']
        self.setup = details['setup']
        self.cleanup = details['cleanup']

        # Some predefined test stats
        self.testcount = len(self.tests)
        self.sCount = 0
        self.fCount = 0
        self.start = 0
        self.brk = False
    
    # Function called when a test succeeds
    def success(self):

        # Increase the number of succeeded tests by one
        self.sCount += 1

        # Give out the passed message
        print(f'{colorama.Fore.GREEN}Passed{colorama.Fore.RESET}')

        # Print the time taken
        print(f'\tTest completed in {colorama.Fore.LIGHTCYAN_EX}{str(time.time() - self.sTime)[:4]}s{colorama.Fore.RESET}\n')
    
    # Function called when a test fails
    def failure(self, test):

        # Increase the number of tests failed by one
        self.fCount += 1

        # Give the message saying 'failed'
        print(f'{colorama.Fore.RED}Failed{colorama.Fore.RESET}')
        print('\t\tThe following test failed: ')

        # Give info about the failed test
        print(f'\n\t\t\tTest name: {colorama.Fore.LIGHTWHITE_EX}{test.name}{colorama.Fore.RESET}')
        print(f'\t\t\tTest function: {colorama.Fore.LIGHTWHITE_EX}{test.testFunc}{colorama.Fore.RESET}')
        print(f'\t\t\tExpected value: {colorama.Fore.LIGHTWHITE_EX}{test.expectedVal}{colorama.Fore.RESET}')
        print(f'\t\t\tInstead got: {colorama.Fore.LIGHTWHITE_EX}{test.ret_value}{colorama.Fore.RESET}\n')

        # Time taken to complete the test
        print(f'\tTest completed in {colorama.Fore.LIGHTCYAN_EX}{str(time.time() - self.sTime)[:4]}s{colorama.Fore.RESET}\n')

        print(colorama.Back.RED+colorama.Fore.WHITE, 'One of the tests failed. Aborting...', colorama.Fore.RESET, colorama.Back.RESET)
        self.brk = True

    # Function to run all the tests defined
    def run(self):

        # Print the current test suite name
        print(
            colorama.Fore.LIGHTWHITE_EX,
            '='*10,
            f'Running test suite: {self.name}',
            '='*10, colorama.Fore.RESET,
            '\n'
        )

        # If the startp tasks are defined
        if self.setup:
            print(colorama.Fore.LIGHTBLUE_EX, 'Running setup tasks...', colorama.Fore.RESET, end='')
            self.setup() # pylint: disable=not-callable
            print(colorama.Fore.BLUE, 'Done\n', colorama.Fore.RESET)

        # Time at which test started
        self.start = time.time()

        # Loop through all the tests
        for i in range(self.testcount):

            if not self.brk:
                # Print the name of the current test case
                print(
                    f' Running test case {colorama.Fore.YELLOW + str(i + 1) + " of %i" % self.testcount}\
                    {colorama.Fore.RESET}...', end=' '
                )

                # Run the test case
                self.exec_test(self.tests[i])

        # If we need to cleanup
        if self.cleanup:
            print(
                colorama.Fore.LIGHTBLUE_EX,
                'Running cleanup tasks...',
                colorama.Fore.RESET, end=''
            )
            self.cleanup() # pylint: disable=not-callable
            print(colorama.Fore.BLUE, 'Done\n', colorama.Fore.RESET)

            # This will be done only if the test is being run by one of the modules
            if self.brk:
                raise AssertionError()

        # Print the total time taken to complete all tests
        print(
            f'\n Completed all tests in {colorama.Fore.LIGHTCYAN_EX}\
                {str(time.time() - self.start)[:4]}s\
                {colorama.Fore.RESET}'
            )

        # Other info about the test suite
        print(
            colorama.Fore.GREEN, f' {self.sCount}{colorama.Fore.RESET} of {self.testcount} passed'
        )
        print(
            colorama.Fore.RED, f' {self.fCount}{colorama.Fore.RESET} of {self.testcount} failed'
        )
        print(
            colorama.Fore.LIGHTWHITE_EX, '='*(42+len(str(self.name))),colorama.Fore.RESET, '\n'
        )
    
    # Function to execute the test
    def exec_test(self, test):

        # Time at which the test was started
        self.sTime = time.time()

        # Call success fnction if the test was succesfull failure function otherwise
        self.success() if test.exec() else self.failure(test)


# The class to specify a single test case
class TestCase:
    def __init__(self, testFunc, expectedVal=0, op='eq', name=None):
        self.name = name # Name of the test or None
        self.testFunc = testFunc # The function whose return value is to be tested
        self.expectedVal = expectedVal # The expected return value of the function
        self.op = op # The operation to be performed

    # Function that executes the test case
    def exec(self):

        # Don't crash in case of an exception
        try:

            # If we want to check if the given function
            # raises a certain exception
            if self.op == 'exception':

                try:
                    # Try to call the function
                    self.ret_value = self.testFunc()

                    # If the function raised an exception then this part will 
                    # never get executed, so if it is getting executed, then
                    # the test has failed
                    self.expectedVal = f'Exception of the type: {self.expectedVal}'
                    return False

                except Exception as e:

                    # If the function raised the exception of the expected type
                    if self.expectedVal in str(type(e)):
                        return True # Test success

                    # Otherwise test failed
                    else:

                        # Return the type of exception we got instead
                        self.ret_value = str(type(e))
                        return False

            # Other kinds of tests
            else:

                # Call the function and store the return value
                self.testVal = self.testFunc()
                self.ret_value = self.testVal

                # If we want to test that whether the return value
                # is equal to expected value
                if self.op == 'eq':

                    # If it is,  success!
                    if self.testVal == self.expectedVal:
                        return True
                    else:

                        # Test failed otherwise
                        return False

                # To test if the return value is not
                # equal to expected value.
                # (Useless)
                elif self.op == 'ne':
                    if self.testVal != self.expectedVal:
                        return True
                    else:
                        return False

                # To test if the return value is exactly True
                elif self.op == 'isTrue':

                    # Set the expected value to True
                    self.expectedVal = True

                    # Actual comparison
                    if self.testVal == True:
                        return True
                    else:
                        return False

                # If the return value is expected to be
                # exactly False, not even None
                elif self.op == 'isFalse':

                    # Set the expected value to False
                    self.expectedVal = False
                    if self.testVal == False:
                        return True
                    else:
                        return False

                # Wrong test type specified, mark as failed
                else:
                    self.ret_value = f'No such test type: {self.op}'
                    return False
        
        # The test function failed with some exception
        # Return false with the traceback
        except:
            self.ret_value = f'Failed with exception: \n{traceback.format_exc()}'
            return False

