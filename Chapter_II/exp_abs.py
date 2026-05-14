# Bài toán: hệ thống thanh toán

# Mỗi hệ thống ngân hàng ViettinBank, momo, thẻ tín dụng
# Đều tuân theo(quy luật) khi người dùng chuyển tiền

# quy luật:
# 1. kiểm tra số tài khoản
# 2. kiểm tra số dư 
# 3. chuyển tiền
# 4. tính phí giao dịch

from abc import ABC, abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class PaymentViettinBank(Payment):
    def __init__(self, account_number, balance):
        super().__init__()
        self.account_number = account_number
        self.balance = balance

    def check_account_number(self):
        if self.account_number == '00000000':
            return False
        elif len(self.account_number) < 8:
            return False
        elif len(self.account_number) > 13:
            return False
        else:
            return True

    def check_balance(self, amount):
        if self.balance < 2000:
            return False
        elif self.balance < amount:
            return False
        else:
            return True
    
    def transfer_money(self, amount):
        self.balance = self.balance - amount
        return self.balance
    
    def caculate_fee(self):
        return 0

    def pay(self, amount):
        # 1. kiểm tra số tài khoản
        self.check_account_number()
        # 2. kiểm tra số dư
        self.check_balance(amount)
        # 3. chuyển tiền
        self.transfer_money(amount)
        # 4. tính phí giao dịch
        self.caculate_fee()


class PaymentMoMo(Payment):
    def __init__(self, account_number, balance):
        super().__init__()
        self.account_number = account_number
        self.balance = balance
    
    # triển khai hành vi thanh toán(hàm pay cho MoMo)

class PaymentCredit(Payment):
    def __init__(self, account_number, balance):
        super().__init__()
        self.account_number = account_number
        self.balance = balance
    
    # triển khai hành vi thanh toán(hàm pay cho thẻ tín dụng)
