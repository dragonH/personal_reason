"""
    This script is for logger
"""
import logging

logging.basicConfig(level=logging.DEBUG)

def main_logger():
    """
        This function is to main logger
    """
    main_logger = logging.getLogger('main')
    return main_logger

def request_logger():
    """
        This function is to request logger
    """
    request_logger = logging.getLogger('request')
    return request_logger