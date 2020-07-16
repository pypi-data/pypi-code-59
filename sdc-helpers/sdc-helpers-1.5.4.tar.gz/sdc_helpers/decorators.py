"""
   SDC decorators module
"""
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError
from sdc_helpers.slack_helper import SlackHelper


def query_exception_handler(exceptions: tuple = (SQLAlchemyError, )):
    """
        Decorator - handling SqlAlchemy specific exceptions

        args:
            exceptions (Exception): List of exceptions to catch

        return:
            Wrapped function's response
    """
    def query_exception_decorator(function):
        @wraps(function)
        def func_with_exceptions(*args, **kwargs):
            """
                Wrapper function to decorate function with
            """
            try:
                return function(*args, **kwargs)
            except exceptions as ex:
                if ex.__dict__.get('orig') is not None:
                    ex.__dict__['orig'] = 'Server Error: {ex}'.format(
                        ex=str(ex.__dict__['orig'])
                    )
                    raise ex

                raise Exception(
                    'Server Error: {ex}'.format(
                        ex=str(ex)
                    )
                )

        return func_with_exceptions

    return query_exception_decorator

def general_exception_handler(
        logger: SlackHelper,
        exceptions: tuple,
        should_raise: bool = True
    ):
    """
        Decorator - general handling for exceptiions which logs the exception using logger
        and optiionally can raise the error as well.

        Args:
            logger (SlackHelper): logger object of type SlackHelper
            exceptions (tuple): List of exceptions to catch
            should_raise (bool, optional): Should error be raised. Defaults to True.

        return:
            Wrapped function's response
    """
    def general_exception_decorator(function):

        @wraps(function)
        def func_with_exceptions(*args, **kwargs):
            """
                Wrapper function to decorate function with
            """
            try:
                return function(*args, **kwargs)

            except exceptions as ex:
                # reformat log
                reformatted_log_msg = (
                    'Server Error: {ex}'.format(ex=str(ex))
                )

                # emit log
                logger.send_critical(message=reformatted_log_msg)

                # raise error
                if should_raise:
                    raise ex

        return func_with_exceptions

    return general_exception_decorator
