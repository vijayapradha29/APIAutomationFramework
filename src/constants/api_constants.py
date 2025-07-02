class APIConstants(object):
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def patch_put_delete_url(booking_id):
        return "https://restful-booker.herokuapp.com/booking/"+str(booking_id)