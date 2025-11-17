from model.User import User
from model.Vehicle import Vehicle

class Customer(User):
    def __init__(self, user_id: str, fullname: str, phone_number: str, email: str, vehicle: Vehicle = None):
        super().__init__(user_id, fullname, phone_number)
        self._email = email
        self._vehicle = vehicle

    @property
    def email(self):
        return self._email