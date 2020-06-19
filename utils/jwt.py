# author:xblinux


def jwt_response_payload_handler(token, user=None, request=None, role=None):
    return {
        "authenticated": "true",
        'id': user.id,
        "role": role,
        'username': user.username,
        'email': user.email,
        'token': token,
    }