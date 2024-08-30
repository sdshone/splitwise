from typing import List, Dict
from decimal import Decimal
from abc import ABC, abstractmethod
from .user import User

class Expense(ABC):
    
    def __init__(self, expense_id: int, amount: Decimal, description: str, paid_by: User, shared_among: List[User]) -> None:
        self.expense_id = expense_id
        self.amount = amount
        self.description = description
        self.paid_by = paid_by
        self.shared_among = shared_among
    
    @abstractmethod
    def calculate_shares(self) -> Dict[User, Decimal]:
        """
        Abstract method to calculate the share of each user in this expense.
        Must be implemented by subclasses.
        """
        pass
    
class EqualExpense(Expense):
    
    def calculate_shares(self) -> Dict[User, Decimal]:
        """Calculate equal shares for each user in the shared list."""
        num_users = len(self.shared_among)
        share_amount = self.amount // num_users
        return { user: share_amount for user in self.shared_among }