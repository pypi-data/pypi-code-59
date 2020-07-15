import pytest
from model_bakery import baker

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN

pytestmark = pytest.mark.django_db


@pytest.fixture
def member(django_user_model):
    return baker.make(django_user_model)


def test_admin_user_can_create_memberships(admin_client, project, member):
    response = create_membership(admin_client, project, member)

    assert response.status_code == HTTP_201_CREATED


def test_user_without_permission_can_create_memberships(client, project, member):
    response = create_membership(client, project, member)

    assert response.status_code == HTTP_201_CREATED


def test_anonymous_user_cannot_create_memberships(anonymous_client, project, member):
    response = create_membership(anonymous_client, project, member)

    assert response.status_code == HTTP_403_FORBIDDEN


def create_membership(client, project, member, is_coordinator=False):
    return client.post(
        reverse('membership-list'),
        data=dict(project=project.id, user=member.id, is_coordinator=is_coordinator)
    )
