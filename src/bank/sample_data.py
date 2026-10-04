"""Synthetic sample data. Safe to paste into prompts."""

from .transactions import Transaction

SAMPLE_TRANSACTIONS = [
    Transaction("ACC-001", 5000.00, "Opening deposit"),
    Transaction("ACC-001", -1200.50, "Airtime purchase"),
    Transaction("ACC-002", 300.00, "Transfer in"),
    Transaction("ACC-002", -75.25, "POS payment"),
]
