from unittest.mock import patch
from db import get_db_host

def test_host_configured_properly():
    with patch ("os.getenv") as mock_getenv:
        mock_getenv.return_value = "mock_db_host"
        host_string = get_db_host()
        assert host_string == "mysql://mock_db_host"


def test_host_does_not_exist():
    with patch ("os.getenv") as mock_getenv:
        mock_getenv.return_value = None
        host_string = get_db_host()
        assert host_string == None


def test_host_empty_string():
    with patch ("os.getenv") as mock_getenv:
        mock_getenv.return_value = ""
        host_string = get_db_host()
        assert host_string == None
