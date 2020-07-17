from eo_lib.service.teams.service import *
from eo_lib.application.abstract_application import AbstractApplication

class ApplicationPerson(AbstractApplication):
	def __init__(self):
		super().__init__(PersonService())
	
class ApplicationTeamMember(AbstractApplication):
	def __init__(self):
		super().__init__(TeamMemberService())
	
class ApplicationOrganization_Role(AbstractApplication):
	def __init__(self):
		super().__init__(Organization_RoleService())
	
class ApplicationTeamMembership(AbstractApplication):
	def __init__(self):
		super().__init__(TeamMembershipService())
	
class ApplicationTeam(AbstractApplication):
	def __init__(self):
		super().__init__(TeamService())
	
class ApplicationProjectTeam(AbstractApplication):
	def __init__(self):
		super().__init__(ProjectTeamService())
	
class ApplicationProject(AbstractApplication):
	def __init__(self):
		super().__init__(ProjectService())
	
