from .lib import _StoppingProblem 
from .schema import validate

"""
Defines the core interface to the library.
"""


class StoppingProblem:
    
    @staticmethod
    def from_config(config={}):
        """[summary]

        Args:
            config (dict): Configuration

        Returns:
            [type]: [description]
        """
        print("Stand-in for validation")

        errors = validate(config)

        if len(errors) > 0:
            msg = "Invalid config. Errors: "
            for error in errors:
                msg = msg + "\n{}".format(error)
            raise AttributeError(msg)

        return _StoppingProblem(**config)

    @staticmethod
    def get_opts():
        """Get options for a user interface. 
        The choices for each option can be passed to the StoppingProblem constructor.

        Returns:
            [type]: [description]
        """
        options = {}
        for key in _StoppingProblem.modules:
            if len(_StoppingProblem.modules[key].__subclasses__()) > 0:
                options[key] = _StoppingProblem.modules[key].opts()
        return options


    @staticmethod
    def get_config(opts=None):

        if opts == None:
            return dict(_StoppingProblem())
        else:

            for key in opts:
                opts[key] = {"type": opts[key]}

            return dict(_StoppingProblem(**opts))



if __name__ == "__main__":
    """Reference usage of the library.
    Shows high-level application code example using default values.
    """
    pass

