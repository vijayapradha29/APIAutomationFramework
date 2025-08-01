

import requests
import pytest
from src.helpers.api_requests_wrapper import post_requests,put_requests,delete_requests
from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.payload_manager import payload_create_token, payload_create_booking
from src.helpers.common_verification import verify_http_status_code, verify_response_should_not_be_none







@pytest.fixture
def create_token():
        response=post_requests(url=APIConstants().create_token(),auth=None,headers=Utils().common_headers_json(),payload=payload_create_token(),in_json=False)
        print(response)
        verify_http_status_code(response,200)
        print(response.status_code)
        token=response.json()["token"]
        print(token)
        verify_response_should_not_be_none(token)
        return token

@pytest.fixture
def create_booking():
        response=post_requests(url=APIConstants().create_booking(),auth=None,headers=Utils().common_headers_json(),payload=payload_create_booking(),in_json=False)
        print(response)
        verify_http_status_code(response,200)
        bookingid=response.json()["bookingid"]
        verify_response_should_not_be_none(bookingid)
        print(bookingid)
        return bookingid