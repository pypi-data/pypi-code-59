from rest_framework.reverse import reverse
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED


def test_list_memberships_not_provided(admin_client):
    response = list_memberships(admin_client)

    assert_method_not_allowed(response)


def test_retrieve_memberships_not_provided(client, membership):
    response = retrieve_membership(client, membership)

    assert_method_not_allowed(response)


def list_memberships(client):
    return client.get(reverse('membership-list'))


def retrieve_membership(client, membership):
    return client.get(reverse('membership-detail', kwargs=dict(pk=membership.pk)))


def assert_method_not_allowed(response):
    assert response.status_code == HTTP_405_METHOD_NOT_ALLOWED
