from decimal import Decimal
from models.user import User
from models.group import Group
from models.expense import EqualExpense

user1 = User(user_id=1, name="Alice", email="alice@example.com")
user2 = User(user_id=2, name="Bob", email="bob@example.com")
user3 = User(user_id=3, name="Charlie", email="charlie@example.com")
user4 = User(user_id=4, name="David", email="david@example.com")

group = Group(group_id=1, name="Trip to Paris", members=[user1, user2, user3, user4])

equal_expense = EqualExpense(
    expense_id=1,
    amount=Decimal('150.00'),
    description="Dinner in Paris",
    paid_by=user1,
    shared_among=[user1, user2, user3, user4]
)

group.add_expense(expense=equal_expense)

print(group)

for user in group.members:
    print(f"{user.name} balance: {user.balance}")