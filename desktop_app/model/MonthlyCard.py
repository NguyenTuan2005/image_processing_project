from datetime import datetime, date

from desktop_app.model.Card import Card
from desktop_app.model.Customer import Customer


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