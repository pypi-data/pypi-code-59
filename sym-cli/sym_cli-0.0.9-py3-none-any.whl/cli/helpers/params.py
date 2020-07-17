from typing import Dict, NamedTuple, TypedDict

from .config import Config


class Profile(NamedTuple):
    display_name: str
    region: str
    arn: str


class OrgParams(TypedDict, total=False):
    okta: Dict[str, str]
    profiles: Dict[str, Profile]


PARAMS: Dict[str, OrgParams] = {
    "launch-darkly": {
        "okta": {
            "aws_saml_url": "home/amazon_aws/0oaj4aow7gPk26Fy6356/272",
            "mfa_provider": "OKTA",
            "mfa_factor_type": "push",
            "assume_role_ttl": "1h",
            "session_ttl": "15m",
        },
        "profiles": {
            "prod": Profile(
                display_name="Prod",
                region="us-east-1",
                arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-production",
            ),
            "staging": Profile(
                display_name="Staging",
                region="us-east-1",
                arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-staging",
            ),
            "catfood": Profile(
                display_name="Catfood",
                region="us-east-1",
                arn="arn:aws:iam::554582317989:role/ops/SSHAdmin-catamorphic",
            ),
            "prod-intuit": Profile(
                display_name="Prod: Intuit",
                region="us-west-2",
                arn="arn:aws:iam::527291094460:role/ops/SSHAdmin-production",
            ),
            "staging-intuit": Profile(
                display_name="Staging: Intuit",
                region="us-west-2",
                arn="arn:aws:iam::527291094460:role/ops/SSHAdmin-staging",
            ),
        },
    }
}


def get_org_params() -> OrgParams:
    config = Config()
    return PARAMS[config["org"]]


def get_okta_section() -> Dict[str, str]:
    return get_org_params()["okta"]


def get_profiles() -> Dict[str, Profile]:
    return get_org_params()["profiles"]


def get_profile(resource: str) -> Profile:
    return get_profiles()[resource]
