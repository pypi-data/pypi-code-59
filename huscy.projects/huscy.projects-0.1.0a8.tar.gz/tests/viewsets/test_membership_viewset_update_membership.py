from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN


def test_admin_user_can_update_memberships(admin_client, membership):
    assert not membership.user.has_perm('change_project', membership.project)

    response = update_membership(admin_client, membership)

    assert response.status_code == HTTP_200_OK
    assert membership.user.has_perm('change_project', membership.project)


def test_user_without_permission_can_update_memberships(client, membership):
    assert not membership.user.has_perm('change_project', membership.project)

    response = update_membership(client, membership)

    assert response.status_code == HTTP_200_OK
    assert membership.user.has_perm('change_project', membership.project)


def test_anonymous_user_cannot_update_memberships(anonymous_client, membership):
    assert not membership.user.has_perm('change_project', membership.project)

    response = update_membership(anonymous_client, membership)

    assert response.status_code == HTTP_403_FORBIDDEN
    assert not membership.user.has_perm('change_project', membership.project)


def update_membership(client, membership):
    return client.put(
        reverse('membership-detail', kwargs=dict(pk=membership.id)),
        data=dict(
            project=membership.project.id,
            user=membership.user.id,
            is_coordinator=False,
            has_write_permission=True,
        ),
    )
