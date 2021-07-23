from sqlalchemy.orm import Session

from src.applications.model.account import Account


class AccountEntity:
    def __init__(self, db: Session):
        self.db = db

    def get_accounts(self):
        return self.db.query(Account).all()