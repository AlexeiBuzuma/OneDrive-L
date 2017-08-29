import onedrivesdk


class AuthProvider(onedrivesdk.AuthProvider):
    def check_saved_session_exists(self):
        return self._session_type.check_saved_session_exists()
