from datetime import datetime, date
from typing import Set, Dict


class Card:
    def __init__(self, card_id: str, time_entry: datetime, time_exit: datetime = None, status: str = "active"):
        self._card_id = card_id
        self._time_entry = time_entry
        self._time_exit = time_exit
        self._status = status

    @property
    def card_id(self):
        return self._card_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: str):
        if value not in ["active", "expired", "closed"]:
            raise ValueError("Trạng thái không hợp lệ")
        self._status = value

    def calculate_fee(self):
        pass

    def update_exit_time(self, exit_time: datetime) -> None:
        self._time_exit = exit_time

    def duration(self) -> int:
        if self._time_exit and self._time_entry:
            return int((self._time_exit - self._time_entry).total_seconds() / 60)
        return 0


class SingleCard(Card):
    def __init__(self, card_id: str, time_entry: datetime, plate_number: str):
        super().__init__(card_id, time_entry)
        self._plate_number = plate_number

    @property
    def plate_number(self):
        return self._plate_number

    def method(self, type):
        pass


class MonthlyCard(Card):
    def __init__(self, card_id: str, expiry_date: date, customer: 'Customer', is_paid: bool):
        super().__init__(card_id, datetime.now())
        self._expiry_date = expiry_date
        self._customer = customer
        self._is_paid = is_paid

    @property
    def expiry_date(self):
        return self._expiry_date

    def is_valid(self) -> bool:
        return date.today() <= self._expiry_date


class Payment:
    def __init__(self, payment_id: str, card: Card, amount: float, method: str, paid_at: datetime):
        self._id = payment_id
        self._card = card
        self._amount = amount
        self._method = method
        self._paid_at = paid_at

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value: float):
        if value < 0:
            raise ValueError("Số tiền không thể âm")
        self._amount = value


class Vehicle:
    def __init__(self, vehicle_id: str, type: str, plate_number: str):
        self._vehicle_id = vehicle_id
        self._type = type
        self._plate_number = plate_number

    @property
    def plate_number(self):
        return self._plate_number

    def method(self, type):
        pass


class User:
    def __init__(self, user_id: str, fullname: str, phone_number: str):
        self._id = user_id
        self._fullname = fullname
        self._phone_number = phone_number

    @property
    def fullname(self):
        return self._fullname


class Customer(User):
    def __init__(self, user_id: str, fullname: str, phone_number: str, email: str, vehicle: Vehicle = None):
        super().__init__(user_id, fullname, phone_number)
        self._email = email
        self._vehicle = vehicle

    @property
    def email(self):
        return self._email


class Staff(User):
    def __init__(self, user_id: str, fullname: str, phone_number: str, password: str, role: int):
        super().__init__(user_id, fullname, phone_number)
        self._password = password
        self._role = role

    def check_password(self, password: str) -> bool:
        return self._password == password


class AiModel:
    def __init__(self):
        pass


class Application:
    def __init__(self):
        self._users: Set[User] = set()
        self._cards: Set[Card] = set()
        self._vehicles: Set[Vehicle] = set()
        self._payments: Set[Payment] = set()
        self._ai_model = AiModel()

    def calculate_total_revenue(self):
        pass

    def statistic_revenue_by_month(self):
        pass

    def check_in(self, card_id: str) :
        pass

    def check_out(self, card_id: str) -> None:
        pass

    def detect_plate(self, card: Card) -> None:
        pass
