"""
    This script is to initialize libs
"""
from ._request import send_request
from ._logger import main_logger, request_logger

__all__ = [
    'send_request',
    'main_logger',
    'request_logger'
]