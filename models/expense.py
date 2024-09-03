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

class PercentageExpense(Expense):

    def __init__(self, expense_id: int, amount: Decimal, description: str, paid_by: User, shared_among: List[User], percentages: Dict[User, Decimal]) -> None:
        super().__init__(expense_id, amount, description, paid_by, shared_among)
        self.percentages = percentages

    def calculate_shares(self) -> Dict[User, Decimal]:
        """Calculate shares based on percentage distribution."""
        return { user: (self.amount * (self.percentages[user]/Decimal('100'))) for user in self.shared_among }

class ExactExpense(Expense):
    def __init__(self, expense_id: int, amount: Decimal,  description: str , paid_by: User, shared_among: List[User], exact_shares: Dict[User, Decimal]):
        super().__init__(expense_id, amount, description, paid_by, shared_among)
        self.exact_shares = exact_shares

    def calculate_shares(self) -> Dict[User, Decimal]:
        """Calculate shares based on exact amounts provided."""
        # Single Responsibility Principle: Calculation logic is contained within the class
        return self.exact_shares
