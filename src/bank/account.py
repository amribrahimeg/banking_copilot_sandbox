"""A minimal bank account with deposits and withdrawals (synthetic data only)."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""


class Account:
    def __init__(self, account_id: str, balance: float = 0.0) -> None:
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds.")
        self.balance -= amount
        return self.balance
