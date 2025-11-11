from desktop_app.db.database import Database
from typing import Set

from desktop_app.model.Card import Card

class CardDAO:
    def __init__(self):
        self.__db = Database()

    def get_all(self) -> Set[Card]:
        conn = self.__db.connect()
        cursor = conn.cursor();
        cursor.execute('SELECT * FROM cards')
        rows = cursor.fetchall()

        return set([Card(row.id,row.entry_time,row.exit_time,status=None) for row in rows])

if __name__ == '__main__':
    cardDao = CardDAO()
    print(cardDao.get_all())

