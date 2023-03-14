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
    
    #def __get_account(self, name):
    #    for acc in self.accounts:
    #        if acc.name == name:
    #            return self.accounts.pop(name)
    #    return None
    
    #def __find_atribute(self, name):
    #    for acc in self.accounts:
    #        if acc.__dict__.pop(name):
    #            return True
    #    return False

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured"""
        if not AccountChecker.account_is_valid(new_account):
            print("ERROR: Account not valid.")
            return False
        if self.__account_exists(new_account.name):
            print("ERROR: Account already exists.")
            return False
        self.accounts.append(new_account)
        return True

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
                self.__account_exists(name):
            #print("TR:> ", self.accounts[0])
            ##for index, acc in enumerate(self.accounts):
            ##    print(len(acc.__dict__))
            ##    for x in reversed(range(0, len(acc.__dict__))):
            ##        print("TR> ", self.accounts[index].__dict__[x])
            #for index, atr in reversed(list(enumerate(self.accounts[name].__dict__))):
            #    if atr.startswith("b"):
            #        del self.accounts[name].__dict__[index]
            #atr = self.accounts[name].__dict__
            #if not hasattr(self.accounts[name], "zip"):
            #    self.accounts[name].zip = ""
            #if not hasattr(self.accounts[name], "addr"):
            #    self.accounts[name].addr = ""
            return True
        return False

            


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
        if not hasattr(acc, "name") or\
        not hasattr(acc, "id") or\
        not hasattr(acc, "value"):
            return False
        return True

    def account_is_corrupted(acc: Account):
        if len(acc.__dict__) % 2 == 0:
            print("ERROR: Account has odd atributes.")
            return True
        if AccountChecker.__find_b_atribute(acc):
            print("ERROR: Has an atribute starting with B")
            return True
        if not AccountChecker.__find_atr(acc, 'zip'):
            print("ERROR: No ZIP")
            return True
        if not AccountChecker.__find_atr(acc, 'addr'):
            print("ERROR: No ADDR")
            return True
        if not AccountChecker.__check_mandatory_atr(acc):
            print("ERROR: Not mandatory atributes.")
            return True
        if not isinstance(acc.name, str):
            print("ERROR: name is not a string")
            return True
        if not isinstance(acc.id, int):
            print("ERROR: id is not an int")
            return True
        if (not isinstance(acc.value, int) and not isinstance(acc.value, float)):
            print("ERROR: Incorrect value type.")
            return True
        return False

    def account_is_valid(acc: Account):
        if not isinstance(acc, Account):
            print("ERROR: Account is not an Account instance.")
            return False
        if AccountChecker.account_is_corrupted(acc):
            return False
        return True
        



