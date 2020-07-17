from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from eo_lib.model.teams.models import *
from eo_lib.service.base_service import BaseService

class PersonService(BaseService):
	def __init__(self):
		super(PersonService,self).__init__(Person)
	
class TeamMemberService(BaseService):
	def __init__(self):
		super(TeamMemberService,self).__init__(TeamMember)
	
class Organization_RoleService(BaseService):
	def __init__(self):
		super(Organization_RoleService,self).__init__(Organization_Role)
	
class TeamMembershipService(BaseService):
	def __init__(self):
		super(TeamMembershipService,self).__init__(TeamMembership)
	
class TeamService(BaseService):
	def __init__(self):
		super(TeamService,self).__init__(Team)
	
class ProjectTeamService(BaseService):
	def __init__(self):
		super(ProjectTeamService,self).__init__(ProjectTeam)
	
class ProjectService(BaseService):
	def __init__(self):
		super(ProjectService,self).__init__(Project)
	
