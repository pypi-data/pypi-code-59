from dataclasses import dataclass
from typing import Union
from snowday.objects.account import Role, User


@dataclass
class RoleGrant:
    # https://docs.snowflake.com/en/sql-reference/sql/grant-role.html
    grantee: Union[Role, User]
    subject: Role

    @property
    def grant(self):
        return f"grant role {self.subject.name} to {self.grantee.resource_type} {self.grantee.name};"

    @property
    def revoke(self):
        return f"revoke role {self.subject.name} from {self.grantee.resource_type} {self.grantee.name};"
