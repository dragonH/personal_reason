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

app.login(_company_id=secrets['company_id'], _user_id=secrets['user_id'], _password=secrets['password'])
print(app.session_id)