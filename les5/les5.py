
# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

#     @abstractmethod
#     def validate_payment(self):
#         pass

# class CreditCardPayment(PaymentMethod):
#     def __init__(self, card_number, is_valid=True):
#         self.card_number = card_number
#         self.is_valid = is_valid  

#     def pay(self, amount):
#         if self.validate_payment():
#             print(f"{amount} somon from kard {self.card_number} minused")
#         else:
#             print("Error kard isnt identify")

#     def validate_payment(self):
#         return self.is_valid

# card = input("Enter number of card: ")
# amount = int(input("Enter payment: "))
# payment = CreditCardPayment(card_number=card)
# payment.pay(amount)


# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

#     @abstractmethod
#     def validate_payment(self):
#         pass

# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         self.amount=amount
#         print(f"Paid {self.amount} using card")

#     def validate_payment(self):
#         print("Validating Credit Card")

# card = CreditCard()
# card.validate_payment()  
# card.pay(1500)           



# Create a class PayPal that:
# Implements pay() by printing: Paid {amount} using PayPal

# Implements validate_payment() by printing: Validating PayPal account

# from abc import ABC, abstractmethod
# class PayPal(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
    
#     @abstractmethod
#     def validate_payment(self,account):
#         pass

# class payy(PayPal):
#     def pay(self, amount):
#         print(f'Paid {amount} using PayPal')
    
#     def validate_payment(self, account):
#         print(f'From account {account}')

# pay1=payy()
# pay1.pay(21)
# pay1.validate_payment('Zikirov.05@gmail.com')

# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

#     @abstractmethod
#     def validate_payment(self):
#         pass

# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card")

#     def validate_payment(self):
#         print("Validating Credit Card")

# class PayPal(PaymentMethod):
#     def pay(self, amount):
#         print(f"Paid {amount} using PayPal")

#     def validate_payment(self):
#         print("Validating PayPal account")

# card = CreditCard()
# card.validate_payment()
# card.pay(1000)


# paypal = PayPal()
# paypal.validate_payment()
# paypal.pay(2000)



