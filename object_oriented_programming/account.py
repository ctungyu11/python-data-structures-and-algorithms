"""
## summary:
This module contains classes that represent bank accounts.

## classes:
- Transaction: A class representing a transaction.
- TransactionType: An enumeration of transaction types.
- Account: The base class for all bank accounts.

## functions:
- transfer: Transfer money from one account to another.
"""

from datetime import datetime
from typing import List
from decimal import Decimal
from enum import Enum
from dataclasses import dataclass


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


@dataclass
class Transaction:
    """A class representing a transaction."""
    amount: Decimal
    transaction_type: TransactionType
    description: str
    date: int = int(datetime.now().timestamp())


class Account(object):
    """A class representing a bank account."""

    def __init__(self, owner: str, balance: Decimal = Decimal(0)):
        self.owner = owner
        self.balance = balance
        self.create_at = int(datetime.now().timestamp())
        self.transactions: List[Transaction] = []
    
    def deposit(self, amount: Decimal, description: str = "Deposit") -> None:
        """Deposit the given amount into the account."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.transactions.append(Transaction(amount, TransactionType.DEPOSIT, description))
    
    def withdraw(self, amount: Decimal, description: str = "Withdraw") -> None:
        """Withdraw the given amount from the account."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(Transaction(amount, TransactionType.WITHDRAWAL, description))
    
    def __str__(self) -> str:
        return f"{self.owner}'s account with balance {self.balance}"


def transfer(amount: Decimal, source: Account, destination: Account) -> None:
    """Transfer money from one account to another."""
    source.withdraw(amount, f"Transfer to {destination.owner}")
    destination.deposit(amount, f"Transfer from {source.owner}")


if __name__ == "__main__":
    account1 = Account("Alice", Decimal(100))
    account2 = Account("Bob", Decimal(50))
    
    transfer(50, account1, account2)
    
    print(account1)
    print(account2)
    print(account1.transactions)
    print(account2.transactions)
