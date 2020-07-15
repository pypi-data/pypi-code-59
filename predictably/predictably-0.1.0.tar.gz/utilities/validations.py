__author__ = ["Ryan Kuhns"]
__all__ = ["is_tuple_list_like"]

def is_tuple_list_like(a):
    """ Checks if input is tuple or list like
        Parameters
        ----------
        a :    
            Input to check
        Returns
        -------
        bool
            True if successful, False otherwise.
    """
    return isinstance(a, (tuple, list))
    