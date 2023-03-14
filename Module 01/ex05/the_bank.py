# Class copied from the subject
class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def __account_exists(self, name):
        for acc in self.accounts:
            if acc.name == name:
                return True
        return False
    
    def __find_atribute(self, name):
        for acc in self.accounts:
            if acc.__dict__.pop(name):
                return True
        return False

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured"""
        if AccountChecker.account_is_valid(new_account) and\
                not self.__account_exists(new_account.name):
            self.accounts.append(new_account)
            return True
        return False

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if AccountChecker.account_is_valid(origin) and\
                AccountChecker.account_is_valid(dest):
            if origin.name == dest.name:
                return True
            if origin.value >= 0 and\
                    origin.value >= amount:
                origin.value -= amount
                dest.value += amount
                return True
        return False
        

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if isinstance(name, str) and\
                self.__find_atribute(name):
            ?????????????


class AccountChecker():
    def __find_b_atribute(acc:Account):
        for atr in acc.__dict__:
            if atr[0] == 'b':
                return True
        return False

    def __find_atr(acc: Account, name: str):
        for atr in acc.__dict__:
            if atr.startswith(name):
                return True
        return False


    def __check_mandatory_atr(acc: Account):
        if not acc.__dict__.pop("name") or\
        not acc.__dict__.pop("id") or\
        not acc.__dict__.pop("value"):
            return False
        return True

    def account_is_corrupted(acc: Account):
        if len(acc.__dict__) % 2 == 0 or\
                AccountChecker.__find_b_atribute(acc) or\
                not AccountChecker.__find_atr(acc, 'zip') or\
                not AccountChecker.__find_atr(acc, 'addr') or\
                not AccountChecker.__check_mandatory_atr(acc) or\
                not isinstance(acc.name, str) or\
                not isinstance(acc.id, int) or\
                (not isinstance(acc.value, int) or not isinstance(acc.value, float)):
            print("ERROR: Account not valid")

    def account_is_valid(acc: Account):
        if isinstance(acc, Account) and\
                not AccountChecker.account_is_corrupted:
            return True
        return False
        


## TEST
acc = Account("test", arg2="ta2", arg3="ta3")
AccountChecker.account_is_corrupted(acc)