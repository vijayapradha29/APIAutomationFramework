import pytest
import allure
import logging
from src.helpers.api_requests_wrapper import post_requests
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that create booking status and Booking ID shouldn't be null")
    @allure.description("Create a Booking from the Payload and verify that booking ID shouldn't be Null")
    def test_create_booking_positive(self):
        logger = Utils.custom_logger()
        response=post_requests(url=APIConstants().create_booking(),auth=None,payload=payload_create_booking(),in_json=False,headers=Utils().common_headers_json())
        booking_id=response.json()['bookingid']
        logger.info(f"Booking ID received: {booking_id}")
        verify_http_status_code(response_data=response,expect_data=200)
        verify_response_should_not_be_none(booking_id)
        logger.info("This is Info Log")