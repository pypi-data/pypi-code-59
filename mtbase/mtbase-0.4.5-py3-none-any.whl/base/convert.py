'''Registry to store all the conversion functions from class A to class B.'''


__all__ = ['ConversionRegistry', 'the_conversion_registry']


class ConversionRegistry(object):
    '''A registry to store all the conversion functions from class A to class B.'''

    def __init__(self):
        self.registry = {}

    def add(self, from_cls, to_cls, func, convertible_func):
        '''Adds a function that converts from class A to class B to the registry.

        Parameters
        ----------
        from_cls : class
            class to convert from
        to_cls : class
            class to convert to
        func : function
            a function of the form `def func(a: A) -> B` to convert an instance of class A to class B
        convertible_func : function, optional
            a function of the form `def func(a: A) -> boolean` to check an instance of class A is convertible to class B. If not provided, the default is a function that returns True.

        Returns
        -------
        True if the conversion had not existed before the operation was invoked and that the function `func` has been added. False otherwise. 
        '''
        key = (from_cls, to_cls)
        if convertible_func is None:
            convertible_func = lambda x: True
        if key in self.registry:
            return False
        self.registry[key] = (func, convertible_func)
        return True


    def get(self, from_cls, to_cls):
        '''Retrieves the function that converts from class A to class B.
        Parameters
        ----------
        from_cls : class
            class to convert from
        to_cls : class
            class to convert to

        Returns
        -------
        (func, convertible_func) or (None, None)
            the registered conversion function and the registered function to check if the conversion works for a given instance. If they are not registered, (None, None) is returned.
        '''
        key = (from_cls, to_cls)
        return self.registry.get(key, (None, None))


the_conversion_registry = ConversionRegistry()
