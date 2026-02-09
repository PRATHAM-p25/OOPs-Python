class Payment:
    def pay(self):
        print("Processing generic payment...")



class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay.")



class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe.")



class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card.")



p1 = Payment()
p2 = GooglePay()
p3 = PhonePe()
p4 = CreditCard()


p1.pay()
p2.pay()
p3.pay()
p4.pay()