from typing import List
from .user import User
from .expense import Expense
from decimal import Decimal

class Group:
    
    def __init__(self, group_id: int, name: str, members: List[User]) -> None:
        self.group_id = group_id
        self.name = name
        self.members = members
        self.expenses: List[Expense] = []

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)
        self.update_balances(expense)

    def update_balances(self, expense: Expense) -> None:
        shares = expense.calculate_shares()
        for user, share in shares.items():
            self._update_user_balance(expense.paid_by, user, share)

    def _update_user_balance(self, paid_by: User, owes_to: User, amount: Decimal):
        """Helper function to update balances between two users."""
        paid_by.balance[owes_to.user_id] = paid_by.balance.get(owes_to.user_id, Decimal('0.00')) + amount
        owes_to.balance[paid_by.user_id] = owes_to.balance.get(paid_by.user_id, Decimal('0.00')) - amount

    def __repr__(self) -> str:
        return f"Group(id={self.group_id}, name={self.name}, members={len(self.members)}, expenses={len(self.expenses)})"