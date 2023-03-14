from the_bank import Account
from the_bank import Bank
from the_bank import AccountChecker

## TEST
#acc = Account("test", arg2="ta2", arg3="ta3")
#AccountChecker.account_is_corrupted(acc)
#print(acc.__dict__)
acc1 = Account("acc1", zip="z1", addr="a1") #valid account
acc2 = Account(name="acc2", zip="z2", addr="a2", test="a", bref="asdf") #valid account

print("False: ", AccountChecker.account_is_corrupted(acc1))
#print("True: ", AccountChecker.account_is_corrupted(acc2))
print("True: ", AccountChecker.account_is_valid(acc1))
print("False: ", AccountChecker.account_is_valid(acc2))
print("---")
bank1 = Bank()
print("True: ",bank1.add(acc1))
print("False: ", bank1.add("no"))
print("False: ", bank1.add(acc2))
bank1.accounts.append(acc2)
print(bank1.fix_account("acc2"))