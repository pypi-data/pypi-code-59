# Copyright © 2020 Red Hat Inc., and others.
#
# This file is part of Bodhi.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""Defines API endpoints related to GraphQL objects."""
import graphene
from cornice import Service
from webob_graphql import serve_graphql_request

from bodhi.server.config import config
from bodhi.server.graphql_schemas import Release, ReleaseModel


graphql = Service(name='graphql', path='/graphql', description='graphql service')


@graphql.get()
@graphql.post()
def graphql_get(request):
    """
    Perform a GET request.

    Args:
        request (pyramid.Request): The current request.
    Returns:
        The GraphQL response to the request.
    """
    context = {'session': request.session}
    return serve_graphql_request(
        request, schema, graphiql_enabled=config.get('graphiql_enabled'),
        context_value=context)


class Query(graphene.ObjectType):
    """Allow querying objects."""

    allReleases = graphene.List(Release)
    specificReleases = graphene.Field(lambda: graphene.List(Release), 
        name=graphene.String(), long_name=graphene.String(),
        version=graphene.String(), id_prefix=graphene.String(),
        branch=graphene.String(), dist_tag=graphene.String(),
        stable_tag=graphene.String(), testing_tag=graphene.String(),
        candidate_tag=graphene.String(), pending_signing_tag=graphene.String(),
        pending_testing_tag=graphene.String(), pending_stable_tag=graphene.String(),
        override_tag=graphene.String(), mail_template=graphene.String(),
        id=graphene.Int(), composed_by_bodhi=graphene.Boolean(),
        create_automatic_updates=graphene.Boolean(), testing_repository=graphene.String(),
        state=graphene.String(), package_manager=graphene.String())

    def resolve_allReleases(self, info):
        """Answer Queries by fetching data from the Schema."""
        query = Release.get_query(info)  # SQLAlchemy query
        return query.all()

    def resolve_specificReleases(self, info, **args):
        """Resolving releases with a given argument"""
        query = Release.get_query(info)

        id_prefix = args.get("id_prefix")
        if id_prefix is not None:
	        query = query.filter(ReleaseModel.id_prefix == id_prefix)
	
        name = args.get("name")
        if name is not None:
	        query = query.filter(ReleaseModel.name == name)

        long_name = args.get("long_name")
        if long_name is not None:
	        query = query.filter(ReleaseModel.long_name == long_name)

        version = args.get("version")
        if version is not None:
	        query = query.filter(ReleaseModel.version == version)

        branch = args.get("branch")
        if branch is not None:
	        query = query.filter(ReleaseModel.branch == branch)

        dist_tag = args.get("dist_tag")
        if dist_tag is not None:
	        query = query.filter(ReleaseModel.dist_tag == dist_tag)

        stable_tag = args.get("stable_tag")
        if stable_tag is not None:
	        query = query.filter(ReleaseModel.stable_tag == stable_tag)

        testing_tag = args.get("testing_tag")
        if testing_tag is not None:
	        query = query.filter(ReleaseModel.testing_tag == testing_tag)

        candidate_tag = args.get("candidate_tag")
        if candidate_tag is not None:
	        query = query.filter(ReleaseModel.candidate_tag == candidate_tag)

        pending_signing_tag = args.get("pending_signing_tag")
        if pending_signing_tag is not None:
	        query = query.filter(ReleaseModel.pending_signing_tag == pending_signing_tag)

        pending_testing_tag = args.get("pending_testing_tag")
        if pending_testing_tag is not None:
	        query = query.filter(ReleaseModel.pending_testing_tag == pending_testing_tag)
        
        pending_stable_tag = args.get("pending_stable_tag")
        if branch is not None:
	        query = query.filter(ReleaseModel.pending_stable_tag == pending_stable_tag)

        override_tag = args.get("override_tag")
        if override_tag is not None:
	        query = query.filter(ReleaseModel.override_tag == override_tag)

        mail_template = args.get("mail_template")
        if mail_template is not None:
	        query = query.filter(ReleaseModel.mail_template == mail_template)

        id = args.get("id")
        if id is not None:
	        query = query.filter(ReleaseModel.id == id)

        composed_by_bodhi = args.get("composed_by_bodhi")
        if composed_by_bodhi is not None:
	        query = query.filter(ReleaseModel.composed_by_bodhi == composed_by_bodhi)

        create_automatic_updates = args.get("create_automatic_updates")
        if branch is not None:
	        query = query.filter(ReleaseModel.create_automatic_updates == create_automatic_updates)

        testing_repository = args.get("testing_repository")
        if testing_repository is not None:
	        query = query.filter(ReleaseModel.testing_repository == testing_repository)

        state = args.get("state")
        if state is not None:
	        query = query.filter(ReleaseModel.state == state)

        packager_manager = args.get("package_manager")
        if packager_manager is not None:
	        query = query.filter(ReleaseModel.package_manager == packager_manager)
            
        return query.all()

schema = graphene.Schema(query=Query)
