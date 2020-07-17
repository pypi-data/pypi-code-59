from rest_framework.reverse import reverse
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_403_FORBIDDEN


def test_admin_user_can_delete_memberships(admin_client, membership):
    response = delete_membership(admin_client, membership)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_user_without_permission_can_delete_memberships(client, membership):
    response = delete_membership(client, membership)

    assert response.status_code == HTTP_204_NO_CONTENT


def test_anonymous_user_cannot_delete_memberships(anonymous_client, membership):
    response = delete_membership(anonymous_client, membership)

    assert response.status_code == HTTP_403_FORBIDDEN


def delete_membership(client, membership):
    return client.delete(reverse('membership-detail', kwargs=dict(pk=membership.id)))
