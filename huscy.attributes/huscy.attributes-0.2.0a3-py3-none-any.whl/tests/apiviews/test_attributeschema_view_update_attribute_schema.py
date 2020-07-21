from django.contrib.auth.models import Permission
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN


def test_admin_user_can_update_attribute_schema(admin_client, attribute_schema_v2):
    response = update_attribute_schema(admin_client)

    assert HTTP_200_OK == response.status_code


def test_user_with_permission_can_update_attribute_schema(client, user, attribute_schema_v2):
    update_permission = Permission.objects.get(codename='change_attributeschema')
    user.user_permissions.add(update_permission)

    response = update_attribute_schema(client)

    assert HTTP_200_OK == response.status_code


def test_user_without_permission_cannot_update_attribute_schema(client, attribute_schema_v2):
    response = update_attribute_schema(client)

    assert HTTP_403_FORBIDDEN == response.status_code


def test_anonymous_user_can_update_attribute_schema(anonymous_client, attribute_schema_v2):
    response = update_attribute_schema(anonymous_client)

    assert HTTP_403_FORBIDDEN == response.status_code


def update_attribute_schema(client):
    return client.put(reverse('attributeschema-detail'), data=dict(schema={}), format='json')
