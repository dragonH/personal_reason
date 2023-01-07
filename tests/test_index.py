"""
    This script is for dev
"""
import sys
# sys.path.append('/mnt/d/python/personal_reason')
sys.path.append('.')
from personal_reason import PersonalReason
import re
import json

secrets = None
with open('./secrets.json') as secret_file:
    secrets = json.load(secret_file)

app = PersonalReason(
    _server_endpoint=secrets['server_endpoint']
)

def test_get_server_ip():
    """
        This is for test get company id
    """
    assert app.server_endpoint == secrets['server_endpoint']

session_id = app.login(
    _company_id=secrets['company_id'],
    _user_id=secrets['user_id'],
    _password=secrets['password']
)

def test_get_company_id():
    """
        This is for test get company id
    """
    assert app.company_id == secrets['company_id']

def test_get_user_id():
    """
        This is for test get user id
    """
    assert app.user_id == secrets['user_id']

def test_get_password():
    """
        This is for test get password
    """
    assert app.password == secrets['password']

def test_get_session_id_from_login():
    """
        This is for test get session id from login
    """
    assert re.match(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', app.session_id)