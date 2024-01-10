from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from backend.constants import PERMISSION_DENIED


def jwt_auth_checker(info):
    # Use JWTAuthentication to authenticate the user
    jwt_authentication = JWTAuthentication()
    try:
        user, _ = jwt_authentication.authenticate(info.context)
        if user is None:
            raise Exception(PERMISSION_DENIED)
    except Exception as e:
        raise Exception(PERMISSION_DENIED)

    # Use IsAuthenticated permission to ensure the user is authenticated
    info.context.user = user
    permission_classes = [IsAuthenticated]
    for permission in permission_classes:
        if not permission().has_permission(info.context, None):
            raise Exception(PERMISSION_DENIED)