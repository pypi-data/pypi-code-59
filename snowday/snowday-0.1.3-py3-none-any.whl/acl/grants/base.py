from dataclasses import dataclass
from snowday.acl.grants.util import get_privilege
from snowday.objects.account import Role


@dataclass
class BaseGrant:
    grantee: Role

    @property
    def privilege(self):
        return get_privilege(self.__class__.__name__)

    @property
    def grant(self):
        return f"grant {self.privilege} on {self.subject.resource_type} {self.subject.fqn} to role {self.grantee.name};"

    @property
    def revoke(self):
        return f"revoke {self.privilege} on {self.subject.resource_type} {self.subject.fqn} from role {self.grantee.name};"

