from decimal import Decimal
from models.user import User
from models.group import Group
from models.expense import EqualExpense, ExactExpense, PercentageExpense

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

exact_expense = ExactExpense(
    expense_id=2,
    amount=Decimal('120.00'),
    description="Museum tickets",
    paid_by=user2,
    shared_among=[user1, user2, user3],
    exact_shares={user1: Decimal('40.00'), user2: Decimal('50.00'), user3: Decimal('30.00')},
)
group.add_expense(exact_expense)

percentage_expense = PercentageExpense(
    expense_id=3,
    amount=Decimal('150.00'),
    description="Hotel room",
    paid_by=user3,
    shared_among=[user1, user2, user3, user4],
    percentages={user1: Decimal('20'), user2: Decimal('30'), user3: Decimal('30'), user4: Decimal('20')},
)
group.add_expense(percentage_expense)


print(group)

for user in group.members:
    print(f"{user.name} balance: {user.balance}")