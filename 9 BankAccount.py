# 9. Создайте класс BankAccount, который будет иметь атрибуты balance и interest_rate, а также методы deposit() и withdraw(), 
# изменяющие баланс на указанную сумму, и метод add_interest(), добавляющий проценты к балансу. 
# Реализуйте также метод is_negative(), который будет возвращать True, если баланс отрицательный.


class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, plus):
        self.balance += plus
        return self.balance

    def withraw(self, minus):
        self.balance -= minus
        return self.balance

    def add_interest(self, procent):
        self.balance += self.balance * procent / 100
        return self.balance

    def is_negative(self):
        if self.balance < 0:
            return True
        else:
            return False

priorbank = BankAccount(10000, 10)
print(priorbank.deposit(500))
print(priorbank.withraw(2000))
print(priorbank.add_interest(10))
print(priorbank.is_negative())