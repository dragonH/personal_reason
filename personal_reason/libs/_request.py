"""
    This script is for request module
"""
import requests
import html

def _format_payload(
    _payload: str,
    _action: str,
    _session_id: str
):
    """
        This function is to format payload
    """
    payload_formated = f"""
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>
        <SystemObjectRun xmlns="http://scsservices.net/">
        <args>
            <SessionGuid>{_session_id}</SessionGuid>
            <Action>{_action}</Action>
            <Format>Xml</Format>
            <Bytes />
            <Value>{html.escape(_payload.strip())}
            </Value>
        </args>
    </SystemObjectRun>
</soap12:Body>
</soap12:Envelope>
"""
    return payload_formated

def send_request(
    _server_endpoint: str,
    _request_type: str,
    _action: str,
    _payload: str,
    _session_id: str
):
    """
        This function is to send requet
    """
    headers = {
        "Content-Type": 'application/soap+xml; charset=utf-8'
    }
    payload_format = _format_payload(
        _payload=_payload,
        _action=_action,
        _session_id=_session_id
    )
    if _request_type == 'GET':
        response = requests.get(
            url=_server_endpoint,
            headers=headers,
            data=payload_format
        )
    elif _request_type == 'POST':
        response = requests.post(
            url=_server_endpoint,
            headers=headers,
            data=payload_format
        )
        return response
    else:
        raise Exception('Invalid request type')
