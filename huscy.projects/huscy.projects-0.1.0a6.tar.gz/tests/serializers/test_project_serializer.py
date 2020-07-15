from model_bakery import baker

from huscy.projects.serializer import MembershipSerializer, ProjectSerializer
from huscy.projects.services import add_member


def test_project_serializer(django_user_model, project):
    membership1 = add_member(project, baker.make(django_user_model), is_coordinator=True)
    membership2 = add_member(project, baker.make(django_user_model))

    expected = dict(
        description=project.description,
        id=project.id,
        local_id=project.local_id,
        local_id_name=project.local_id_name,
        members=[
            MembershipSerializer(membership1).data,
            MembershipSerializer(membership2).data,
        ],
        principal_investigator=project.principal_investigator.pk,
        principal_investigator_name=project.principal_investigator.get_full_name(),
        research_unit=project.research_unit.pk,
        research_unit_name=project.research_unit.name,
        title=project.title,
        visibility=project.visibility,
    )

    assert expected == ProjectSerializer(instance=project).data
