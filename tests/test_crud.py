'''
1.create token
2.create booking id
3.update booking
4.delete the booking
'''
import pytest
import allure
import logging
from src.helpers.api_requests_wrapper import put_requests,delete_requests
from src.constants.api_constants import APIConstants
from src.helpers.common_verification import verify_http_status_code
from src.utils.utils import Utils
from src.helpers.payload_manager import payload_create_booking

class TestCrud(object):
    def test_update_booking(self,create_token,create_booking):
        logger=Utils.custom_logger()
        token=create_token
        booking_id=create_booking
        headers = Utils().common_headers_json()
        headers["Cookie"] = f"token={token}"
        response=put_requests(url=APIConstants().patch_put_delete_url(booking_id),auth=None,headers=headers,payload=payload_create_booking(),in_json=False)
        verify_http_status_code(response_data=response,expect_data=200)
        logger.info(f"Token: {token}")
        logger.info(f"Booking ID Created: {booking_id}")
        logger.info(f"Booking with ID {booking_id} updated successfully.")
        logger.info(f"Response Body: {response.json()}")
    def test_delete_booking(self,create_booking,create_token):
        logger=Utils.custom_logger()
        token=create_token
        booking_id=create_booking
        response=delete_requests(url=APIConstants().patch_put_delete_url(booking_id),auth=("admin","password123"),headers=Utils().common_headers_json(),payload=None,in_json=False)
        verify_http_status_code(response_data=response,expect_data=201)
        logger.info(response.status_code)
        logger.info(f"Booking with ID {booking_id } deleted Successfully")