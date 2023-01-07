"""
    This script is is for personal reason core
"""
from personal_reason.libs import send_request, main_logger
# import xml.etree.ElementTree as ET
import xmltodict
import random
import time

class PersonalReason(Exception):
    """
        Personal reason class
    """ 
    logger = main_logger()
    def __init__(
        self,
        _server_endpoint: str,
    ):
        """
            This function is to initialize PersonalReason
        """
        self.server_endpoint = _server_endpoint
        self.session_id = '00000000-0000-0000-0000-000000000000'

    def login(
        self,
        _company_id: str,
        _user_id: str,
        _password: str
    ):
        """
            This function is to process login action and get session id
        """
        self.logger.info('Start to login...')
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
        response = send_request(
            _server_endpoint=self.server_endpoint,
            _request_type='POST',
            _action='Login',
            _payload=login_payload,
            _session_id=self.session_id,
            _payload_type='login'
        )
        original_xml = xmltodict.parse(response.text)
        value_xml = original_xml['soap:Envelope']['soap:Body']['SystemObjectRunResponse']['SystemObjectRunResult']['Value']
        value_as_dict = xmltodict.parse(value_xml)
        self.session_id = value_as_dict['TLoginOutputResult']['SessionGuid']
        self.logger.info('Login successfully')
        return self

    def _format_clock_payload(
        self,
        _latitude_adjusted: str,
        _longitude_adjusted: str,
        _company_id: str,
        _address: str,
        _clock_action_type: str
    ):
        """
            This function is to format clock payload
        """
        clock_action_payload = f"""
<?xml version="1.0" encoding="utf-16"?>
<TExecFuncInputArgs xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <FuncID>ExecuteSwipeData_Web</FuncID>
    <Parameters>
        <Parameter>
            <Name>DutyCode</Name>
            <Value xsi:type="xsd:int">{4 if _clock_action_type == 'clock_in' else 8}</Value>
        </Parameter>
        <Parameter>
            <Name>DutyStatus</Name>
            <Value xsi:type="xsd:int">{4 if _clock_action_type == 'clock_in' else 5}</Value>
        </Parameter>
        <Parameter>
            <Name>GPSLocation</Name>
            <Value xsi:type="xsd:string">{_latitude_adjusted},{_longitude_adjusted}</Value>
        </Parameter>
        <Parameter>
            <Name>CompanyID</Name>
            <Value xsi:type="xsd:string">{_company_id}</Value>
        </Parameter>
        <Parameter>
            <Name>GpsAddress</Name>
            <Value xsi:type="xsd:string">{_address}</Value>
        </Parameter>
        <Parameter>
            <Name>NoCheckOnDutyStatus</Name>
            <Value xsi:type="xsd:boolean">true</Value>
        </Parameter>
    </Parameters>
</TExecFuncInputArgs>
"""
        return clock_action_payload

    def clock_action(
        self,
        _base_latitude: str,
        _base_longitude: str,
        _address: str,
        _clock_action_type: str
    ):
        """
            This function is to process clock action
        """
        self.logger.info('Start to clock in...')
        latitude_adjusted = str(_base_latitude)[:-3] + str(random.randint(1,100)).zfill(3)
        longitude_adjusted = str(_base_longitude)[:-3] + str(random.randint(1,100)).zfill(3)
        if _clock_action_type not in ['clock_in', 'clock_out']:
            raise Exception('Clock action not supported. Must be clock_in or clock_out')
        clock_payload = self._format_clock_payload(
            _latitude_adjusted=latitude_adjusted,
            _longitude_adjusted=longitude_adjusted,
            _company_id=self.company_id,
            _address=_address,
            _clock_action_type=_clock_action_type
        )
        random_sleep_seconds = random.randint(1, 90)
        self.logger.info('start to sleep for %s seconds', random_sleep_seconds)
        # time.sleep(random_sleep_seconds)
        self.logger.info('Finish sleeping for %s seconds', random_sleep_seconds)
        response = send_request(
            _server_endpoint=self.server_endpoint,
            _request_type='POST',
            _action='ExecFunc',
            _payload=clock_payload,
            _session_id=self.session_id,
            _payload_type='clock'
        )
        print(response.text)