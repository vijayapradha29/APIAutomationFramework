import pytest
import allure

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that create booking status and Booking ID shouldn't be null")
    @allure.description("Create a Booking from the Payload and verify that booking ID shouldn't be Null")
    def test_create_booking_positive(self):
        pass