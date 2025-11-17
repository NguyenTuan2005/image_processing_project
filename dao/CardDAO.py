from db.database import Database
from typing import Set

from model.Card import Card

class CardDAO:
    def __init__(self):
        self.__db = Database()

    def get_all(self) -> Set[Card]:
        conn = self.__db.connect()
        cursor = conn.cursor();
        cursor.execute('SELECT * FROM cards')
        rows = cursor.fetchall()

        return set([Card(row.id,row.entry_time,row.exit_time,status='') for row in rows])

