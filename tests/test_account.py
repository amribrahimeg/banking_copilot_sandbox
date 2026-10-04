from src.bank.account import Account, InsufficientFundsError
import pytest


def test_deposit_increases_balance():
    account = Account("ACC-001", 100.0)
    assert account.deposit(50.0) == 150.0


def test_withdraw_too_much_raises():
    account = Account("ACC-001", 100.0)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(500.0)
