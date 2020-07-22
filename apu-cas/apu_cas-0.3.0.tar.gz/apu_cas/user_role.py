from enum import Enum


class UserRole(Enum):
    STUDENT = 1 << 0
    LECTURER = 1 << 1
    ADMIN = 1 << 2

    @staticmethod
    def assert_user_role(object):
        """
        Check if a given object or value is instance of UserRole

        Throws AssertionError on invalid instance
        """
        assert isinstance(object, UserRole), f"Unknown role {object}"
