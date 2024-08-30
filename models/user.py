from typing import Dict
from decimal import Decimal

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.balance: Dict[int, Decimal] = {}  # Balance with other users (user_id -> balance)

    def __repr__(self):
        return f"User(id={self.user_id}, name={self.name}, email={self.email})"
