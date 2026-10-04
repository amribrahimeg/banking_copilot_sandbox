## Goal
Add a `transactions_for(account_id)` helper to `src/bank/transactions.py` that returns
only the transactions for the given account, and cover it with a pytest test.

## Acceptance criteria
- [ ] `transactions_for(account_id, transactions)` returns a list filtered by `account_id`.
- [ ] A pytest test in `tests/test_transactions.py` covers the new behavior.
- [ ] `pytest` passes locally.

## Notes
- Synthetic data only — see `src/bank/sample_data.py`.
- Keep the change small and easy to review.
