from abc import ABC, abstractmethod

class Account(ABC):
    """
    Abstract base class for bank accounts.

    Attributes:
        _account_number (str): The account number.  This is a private attribute.
        _balance (float): The account balance. This is a protected attribute.
    """

    def __init__(self, account_number, initial_balance=0.0):
        """
        Initializes a new account.

        Args:
            account_number (str): The account number.
            initial_balance (float): The initial balance (default: 0.0).
        """
        self._account_number = account_number  # Protected attribute
        self._balance = initial_balance  # Protected attribute

    def deposit(self, amount):
        """
        Deposits money into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount:.2f} into account {self._account_number}")
        else:
            print("Invalid deposit amount.")

    @abstractmethod
    def withdraw(self, amount):
        """
        Abstract method to withdraw money from the account.
        Must be implemented by subclasses.

        Args:
            amount (float): The amount to withdraw.
        """
        pass

    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The account balance.
        """
        return self._balance

    def _set_balance(self, balance):
        """
        Sets the account balance.  This is a protected method.

        Args:
            balance (float): The new balance.
        """
        self._balance = balance


class SavingsAccount(Account):
    """
    Represents a savings account.

    Attributes:
        _interest_rate (float): The annual interest rate. This is a private attribute.
    """

    def __init__(self, account_number, initial_balance=0.0, interest_rate=0.01):
        """
        Initializes a new savings account.

        Args:
            account_number (str): The account number.
            initial_balance (float): The initial balance (default: 0.0).
            interest_rate (float): The annual interest rate (default: 0.01).
        """
        super().__init__(account_number, initial_balance)
        self.__interest_rate = interest_rate  # Private attribute

    def withdraw(self, amount):
        """
        Withdraws money from the savings account.
        Cannot withdraw more than the current balance.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self._account_number}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def calculate_interest(self):
        """
        Calculates and adds interest to the account balance.
        """
        interest = self._balance * self.__interest_rate
        self._balance += interest
        print(f"Added interest of ${interest:.2f} to account {self._account_number}")


class CheckingAccount(Account):
    """
    Represents a checking account.

    Attributes:
        _overdraft_limit (float): The overdraft limit. This is a private attribute.
    """

    def __init__(self, account_number, initial_balance=0.0, overdraft_limit=100.0):
        """
        Initializes a new checking account.

        Args:
            account_number (str): The account number.
            initial_balance (float): The initial balance (default: 0.0).
            overdraft_limit (float): The overdraft limit (default: 100.0).
        """
        super().__init__(account_number, initial_balance)
        self.__overdraft_limit = overdraft_limit  # Private attribute

    def withdraw(self, amount):
        """
        Withdraws money from the checking account, allowing overdraft up to the limit.

        Args:
            amount (float): The amount to withdraw.
        """
        if amount > 0 and (self._balance + self.__overdraft_limit) >= amount:
            self._balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self._account_number}")
        else:
            print("Withdrawal amount exceeds overdraft limit or is invalid.")


# Example Usage
if __name__ == "__main__":
    # Create a SavingsAccount instance
    savings_account = SavingsAccount("SA123", 1000.0, 0.02)
    print(f"Savings Account Balance: ${savings_account.get_balance():.2f}")
    savings_account.deposit(500.0)
    savings_account.withdraw(200.0)
    savings_account.calculate_interest()
    print(f"Savings Account Balance: ${savings_account.get_balance():.2f}")

    # Create a CheckingAccount instance
    checking_account = CheckingAccount("CA456", 500.0, 200.0)
    print(f"Checking Account Balance: ${checking_account.get_balance():.2f}")
    checking_account.withdraw(600.0)  # Overdraft
    print(f"Checking Account Balance: ${checking_account.get_balance():.2f}")
    checking_account.withdraw(200.0)  # Exceeds overdraft limit
    print(f"Checking Account Balance: ${checking_account.get_balance():.2f}")