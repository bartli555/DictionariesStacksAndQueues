required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = user_permissions.issubset(required_permissions)  # subset
# Alternatywnie: user_permissions <= required_permissions

print(has_permissions)