from personal_reason import PersonalReason
import sys
import json

sys.path.insert(0, '/mnt/d/python/personal-reason')
secrets = None
with open('./secrets.json') as secret_file:
    secrets = json.load(secret_file)

app = PersonalReason(
    _server_endpoint=secrets['server_endpoint']
)

app \
    .login(
        _company_id=secrets['company_id'],
        _user_id=secrets['user_id'],
        _password=secrets['password']
    ) \
    .clock_action(
        _base_latitude=secrets['base_latitude'],
        _base_longitude=secrets['base_longitude'],
        _address=secrets['address'],
        _clock_action_type='clock_in'
    )


