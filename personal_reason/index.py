"""
    This script is is for personal reason core
"""
from personal_reason._request import session
# import xml.etree.ElementTree as ET
import xmltodict

class PersonalReason(Exception):
    """
        Personal reason class
    """ 
    def __init__(
        self,
        _server_endpoint: str,
    ):
        self.server_endpoint = _server_endpoint

    def login(
        self,
        _company_id: str,
        _user_id: str,
        _password: str
    ):
        self.company_id = _company_id
        self.user_id = _user_id
        self.password = _password
        login_payload = f"""
<?xml version="1.0" encoding="utf-16"?>
<TLoginInputArgs xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <AppName>App</AppName>
    <CompanyID>{_company_id}</CompanyID>
    <UserID>{_user_id}</UserID>
    <Password>{_password}</Password>
    <LanguageID>en</LanguageID>
    <UserHostAddress />
    <IsSaveSessionBuffer>true</IsSaveSessionBuffer>
    <ValidateCode />
    <OAuthType>NotSet</OAuthType>
    <IsValidateRegister>false</IsValidateRegister>
</TLoginInputArgs>
"""
        response = session(
            _server_endpoint=self.server_endpoint,
            _request_type='POST',
            _action='Login',
            _payload=login_payload
        )
        original_xml = xmltodict.parse(response.text)
        value_xml = original_xml['soap:Envelope']['soap:Body']['SystemObjectRunResponse']['SystemObjectRunResult']['Value']
        value_as_dict = xmltodict.parse(value_xml)
        self.session_id = value_as_dict['TLoginOutputResult']['SessionGuid']
