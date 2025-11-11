from typing import Set

from desktop_app.model.Card import Card
from desktop_app.model.Payment import Payment
from desktop_app.model.User import User
from desktop_app.model.Vehicle import Vehicle


class Application:
    def __init__(self):
        self._users: Set[User] = set()
        self._cards: Set[Card] = set()
        self._vehicles: Set[Vehicle] = set()
        self._payments: Set[Payment] = set()

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