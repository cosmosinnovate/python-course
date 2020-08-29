"""
Creating a credit card system 
Will use Object and List

CreditCard: Object
--------------
Fields will include: Customer, balance, 
list_of_credit_cards: List 
"""

class CreditCard:
    """ Credit card for consumers """
    def __init__(self, customer, bank, acnt: float, limit: int):
        """Create a new credit card instance
        The initial balance is zero
        
        Args:
            customer ([type]):the name of the customer eg. John Bowman
            bank ([type]):  eg. California Savings
            acnt (double):  eg. 5391 0375 9387 5309
            limit (int): credit limit  (measure in your own currency. eg dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0.0

    def get_customer(self):
        """ return customer name"""
        return self._customer

    def get_bank(self):
        """ return bank"""
        return self._bank

    def get_account(self):
        """return account"""
        return self._account

    def get_limit(self):
        """Get credit card limit

        Returns:
            _limit (double): return the credit card limit for individual user
        """
        return self._limit
    
    def get_balance(self):
        """return balance"""
        return self._balance

    def make_payments(self, amount):
        """Customer payments that reduces balance
        
        Args:
            amount (double): user payments to the credit card
        """
        self._balance -= amount

    def charge(self, price):
        """Charge given price assuming sufficient credit limit

        Args:
            price (double): price for things customers buy 
        """
        if price + self._balance > self._limit:  # Charge will exceed limits
            return False  # Cannot accept charge
        else:
            self._balance += price
            return True
