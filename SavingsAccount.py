from BankAccount import BankAccount


class SavingsAccount(BankAccount):

    def deposit(self, amount):
        self.balance += amount
        return f'Вы внесли на счет {amount} сомов'

    def with_draw(self, amount):
        if self.balance < amount:
            return f'Недостаточно средств для для снятия данной суммы {amount}'
        else:
            self.balance -= amount
            return f'Вы сняли деньги в размере {amount} со счета. Остаток в счете {self.balance}'
