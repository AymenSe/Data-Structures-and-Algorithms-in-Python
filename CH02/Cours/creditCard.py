class CreditCard:
    """ A consumer Credit Card class """
    def __init__(self, customer, bank, acnt, limit) -> None:
        """ Create a New card instance
        The initial balance is zero

        customer: the name of the customer 'str'
        bank: the name of the bank 'str'
        acnt: the account id 'str'
        limit: credit limit 'int' 
        
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    # Getters

    def get_customer(self) -> str:
        return self._customer
    
    def get_bank(self) -> str:
        return self._bank

    def get_account(self) -> str:
        return self._account
    
    def get_limit(self) -> int:
        return self._limit
    
    def get_balance(self) -> int:
        return self._balance
    
    # Setters

    def charge(self, price : int) -> bool:
        """ Charge a given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if self._balance + price > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount : int) -> None:
        """ Process customer payment that reduces balance"""
        self._balance -= amount

    
if __name__ == '__main__':
    wallet = []

    wallet.append(
        CreditCard('Aymen Sekhri', 'Wise', '1000 2000 3000 4000', 5000)
    )

    wallet.append(
        CreditCard('XXXX YYYY', 'Payssera', '1111 2222 3333 4444', 2500)
    )

    wallet.append(
        CreditCard('ZZZZ DDDD', 'BNP', '9999 9999 9999 9999', 10000)
    )

    for val in range(1, 20):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(len(wallet)):
        print(f'Customer: {wallet[c].get_customer()}')
        print(f'Bank: {wallet[c].get_bank()}')
        print(f'Account: {wallet[c].get_account()}')
        print(f'Limit: {wallet[c].get_limit()}')
        print(f'Balance: {wallet[c].get_balance()}')
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print(f'New Balance: {wallet[c].get_balance()}')
        print()


