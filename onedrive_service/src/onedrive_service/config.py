import yaml
from .errors import OneDriveConfigError


def _check_config(config) -> None:
    """ Check validity of configurations. """

    # Check existing required sections in configuration file
    required_sections = ("auth", )
    missing_sections = [required_section for required_section in required_sections if required_section not in config]
    if missing_sections:
        raise OneDriveConfigError("Sections '{}' are required. Missing sections: '{}'"
                                  .format(", ".join(required_sections), ", ".join(missing_sections)))

    # Check 'auth' section fields
    required_auth_fields = ("client_id", "client_secret", "redirect_uri", "scopes")
    missing_auth_fields = [field for field in required_auth_fields if field not in config["auth"]]
    if missing_auth_fields:
        raise OneDriveConfigError("Fields '{}' are required in 'auth' section. Missing fields: '{}'"
                                  .format(', '.join(required_auth_fields), ", ".join(missing_auth_fields)))


def load_config(path: str) -> dict:
    """ Load configuration. """

    with open(path) as config_file:
        config = yaml.load(config_file.read())

    _check_config(config)
    return config
