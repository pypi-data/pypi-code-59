import pytest

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from huscy.projects import services, serializer

pytestmark = pytest.mark.django_db


def test_admin_user_can_get_memberships(admin_client, project):
    response = list_memberships(admin_client, project)

    assert response.status_code == HTTP_200_OK


def test_user_without_permission_can_get_memberships(client, project):
    response = list_memberships(client, project)

    assert response.status_code == HTTP_200_OK


def test_anonymous_user_cannot_get_memberships(anonymous_client, project):
    response = list_memberships(anonymous_client, project)

    assert response.status_code == HTTP_403_FORBIDDEN


def test_membership_in_response(client, membership):
    response = list_memberships(client, membership.project)

    assert response.json() == serializer.MembershipSerializer([membership], many=True).data


@pytest.mark.skip
def test_service_function_was_called(mocker, client, project):
    mocker.spy(services, 'get_memberships')

    list_memberships(client, project)

    assert services.get_memberships.call_count == 1


def list_memberships(client, project):
    return client.get(reverse('project-members', kwargs=dict(pk=project.pk)))
