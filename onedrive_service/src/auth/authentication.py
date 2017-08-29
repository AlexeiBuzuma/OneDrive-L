import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer

from .session import Session
from .auth_provider import AuthProvider

redirect_uri = ""
client_secret = ""
client_id = ""
api_base_url = "https://api.onedrive.com/v1.0/"

scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']


def authenticate_one_drive_client(auth_code=None):
    """ Authenticate process for OneDrive.
    """

    http_provider = onedrivesdk.HttpProvider()
    auth_provider = AuthProvider(http_provider, client_id, scopes, session_type=Session)
    client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)

    if auth_provider.check_saved_session_exists():
        auth_provider.load_session()

    else:
        if auth_code is None:
            auth_url = client.auth_provider.get_auth_url(redirect_uri)
            auth_code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)

        auth_provider.authenticate(auth_code, redirect_uri, client_secret)
        auth_provider.save_session()

    return client


def authenticate_one_drive_for_business_client():
    """ Authenticate process for OneDrive for business.
    """

    raise NotImplemented
