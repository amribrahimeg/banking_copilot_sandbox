"""Simple transaction records and summaries (synthetic data only)."""

from dataclasses import dataclass


@dataclass
class Transaction:
    account_id: str
    amount: float          # positive = credit, negative = debit
    description: str


def total_balance(transactions: list[Transaction]) -> float:
    """Return the net sum of all transaction amounts."""
    return sum(t.amount for t in transactions)


# TODO (lab): add a `transactions_for(account_id, transactions)` helper and a test for it.
