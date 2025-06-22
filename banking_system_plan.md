# Banking System OOP Example Plan

The Python code will demonstrate OOP principles by modeling a simple banking system with the following structure:

1.  **`Account` (Abstract Class):**
    *   Attributes: `account_number` (private), `balance` (protected)
    *   Methods:
        *   `__init__(self, account_number, initial_balance)`: Constructor to initialize account number and balance.
        *   `deposit(self, amount)`: Method to deposit money into the account.
        *   `withdraw(self, amount)`: Abstract method to withdraw money from the account.
        *   `get_balance(self)`: Method to return the current balance.
        *   `_set_balance(self, balance)`: Protected method to set the balance.

2.  **`SavingsAccount` (Inherits from `Account`):**
    *   Attributes: `interest_rate` (private)
    *   Methods:
        *   `__init__(self, account_number, initial_balance, interest_rate)`: Constructor to initialize account number, balance, and interest rate.
        *   `withdraw(self, amount)`: Method to withdraw money, ensuring balance doesn't go below zero.
        *   `calculate_interest(self)`: Method to calculate and add interest to the balance.

3.  **`CheckingAccount` (Inherits from `Account`):**
    *   Attributes: `overdraft_limit` (private)
    *   Methods:
        *   `__init__(self, account_number, initial_balance, overdraft_limit)`: Constructor to initialize account number, balance, and overdraft limit.
        *   `withdraw(self, amount)`: Method to withdraw money, allowing overdraft up to the limit.

**OOP Principles Demonstrated:**

*   **Class Definition:** Defining `Account`, `SavingsAccount`, and `CheckingAccount` classes.
*   **Instantiation:** Creating instances of `SavingsAccount` and `CheckingAccount`.
*   **Inheritance:** `SavingsAccount` and `CheckingAccount` inheriting from `Account`.
*   **Polymorphism:** Method overriding of the `withdraw` method in `SavingsAccount` and `CheckingAccount`.
*   **Encapsulation:** Using private attributes (`account_number`, `interest_rate`, `overdraft_limit`) and protected attributes (`balance`).
*   **Abstraction:** `Account` being an abstract class with an abstract `withdraw` method.

**Mermaid Diagram:**

```mermaid
classDiagram
    class Account {
        -account_number: str
        #balance: float
        +__init__(account_number: str, initial_balance: float)
        +deposit(amount: float)
        +withdraw(amount: float)
        +get_balance() : float
        #_set_balance(balance: float)
    }
    class SavingsAccount {
        -interest_rate: float
        +__init__(account_number: str, initial_balance: float, interest_rate: float)
        +withdraw(amount: float)
        +calculate_interest()
    }
    class CheckingAccount {
        -overdraft_limit: float
        +__init__(account_number: str, initial_balance: float, overdraft_limit: float)
        +withdraw(amount: float)
    }
    Account <|-- SavingsAccount
    Account <|-- CheckingAccount