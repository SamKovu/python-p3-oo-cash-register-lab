#!/usr/bin/env python3

class CashRegister:

  def __init__(self,discount=0):
    self.discount=discount
    self.total=0
    self.items=[]
    self.transactions=[]

  def add_item(self,title,price,quantity=1):
    self.total=self.total+price*quantity
    self.transactions.append(price*quantity)
    
    while quantity>0:
      self.items.append(title)
      quantity-=1

  def apply_discount(self):
    if self.discount==0:
      print("There is no discount to apply.")
    else:
      self.total=self.total-(self.total*self.discount/100)
      print(f"After the discount, the total comes to ${self.total:.0f}.")

  def void_last_transaction(self):
    self.total=self.total-self.transactions[-1]
    self.transactions.pop()

    


    
 
