from src.bank.transactions import Transaction, total_balance


def test_total_balance_sums_amounts():
    txns = [
        Transaction("ACC-001", 5000.00, "Opening deposit"),
        Transaction("ACC-001", -1200.50, "Airtime purchase"),
    ]
    assert total_balance(txns) == 3799.50


# TODO (lab): write a test for the new `transactions_for(account_id, transactions)` helper.
