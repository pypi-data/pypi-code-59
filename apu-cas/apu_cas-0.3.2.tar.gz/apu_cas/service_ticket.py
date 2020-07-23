import functools
import typing

import requests
from flask import request, abort, redirect

from .variables import cas_url
from .user_cas_attributes import save_user_cas_attributes, get_user_cas_attributes
from .user_role import UserRole


cas_service_validation_url = f'{cas_url}/cas/p3/serviceValidate?format=json&service=%(service)s&ticket=%(ticket)s'
cas_redirect_url = f"{cas_url}/cas/login?service=%(service)s"


def determine_roles():
    """
    Determine the roles that a user can have according to their CAS user attributes
    :return: role_value
    """
    assert get_user_cas_attributes(), "No CAS Attribute found"

    user_cas_attributes = get_user_cas_attributes()
    member_of_attributes = "".join([
        member_of_attribute.lower() for member_of_attribute in user_cas_attributes.member_of
    ])
    distinguished_name_attributes = "".join([
        distinguished_name_attribute.lower() for distinguished_name_attribute in user_cas_attributes.distinguished_name
    ])
    joined_attributes = member_of_attributes + distinguished_name_attributes
    role_value = 0

    if "ou=students" in joined_attributes:
        role_value = role_value | UserRole.STUDENT.value
    if "ou=academic" in joined_attributes:
        role_value = role_value | UserRole.LECTURER.value
    if "ou=apiit tpm" in joined_attributes:
        role_value = role_value | UserRole.ADMIN.value

    return role_value


def is_authorized_role(restricted_to_roles: typing.Sequence[UserRole]) -> bool:
    if not restricted_to_roles:
        return True

    current_user_role = determine_roles()
    combined_accepted_role_value = 0

    for restricted_to_role in restricted_to_roles:
        combined_accepted_role_value = combined_accepted_role_value | restricted_to_role.value

    return current_user_role & combined_accepted_role_value


def validate_service_ticket():
    ticket = request.args.get('ticket', None)

    if ticket is None:
        return False

    response = requests.get(
        cas_service_validation_url % {"service": request.base_url, "ticket": ticket}
    ).json()['serviceResponse']

    if 'authenticationSuccess' not in response:
        return False

    return response['authenticationSuccess']['attributes']


def has_role(role_to_check: UserRole):
    """
    Check if current user has the given role_to_check
    """
    UserRole.assert_user_role(role_to_check)

    return is_authorized_role([role_to_check])


def require_service_ticket(
        _function: typing.Optional[typing.Callable] = None,
        *,
        restricted_to_roles: typing.Optional[typing.Sequence[UserRole]] = None
):
    """
    Makes decorated endpoint to require CAS service ticket as query string parameter
    """
    restricted_to_roles = restricted_to_roles if restricted_to_roles else []

    if restricted_to_roles is None:
        restricted_to_roles = []
    for restricted_to_role in restricted_to_roles:
        UserRole.assert_user_role(restricted_to_role)

    @functools.wraps(_function)
    def require_service_ticket_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            user_cas_attributes = validate_service_ticket()

            if not user_cas_attributes:
                return redirect(
                    cas_redirect_url % {"service": request.base_url}
                )

            save_user_cas_attributes(user_cas_attributes)

            if not is_authorized_role(restricted_to_roles):
                abort(403, "Insufficient permission to access this service")

            return function(*args, **kwargs)

        return wrapper

    if _function is None:
        return require_service_ticket_decorator
    else:
        return require_service_ticket_decorator(_function)
