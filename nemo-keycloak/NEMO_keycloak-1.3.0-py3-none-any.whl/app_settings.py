# Profile
KEYCLOAK_PERMISSIONS_METHOD = "role"  # 'role' of 'resource'

# Create User if not present
KEYCLOAK_CREATE_DJANGO_USER = False
# Update User with Keycloak user information
KEYCLOAK_UPDATE_DJANGO_USER = False
# Field to look for username in token
KEYCLOAK_TOKEN_USERNAME_FIELD = "sub"
# Use User model permissions, when False use keycloak permissions
KEYCLOAK_USE_USER_MODEL_PERMISSIONS = True
