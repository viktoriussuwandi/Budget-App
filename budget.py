import pandas as pd
import numpy as np
import files

class Category:

  def __init__(self, category=None):
    self.ledger        = []
    self.data_saved    = []
    self.category      = category if category is not None else None
    self.balance       = 0
    self.form_ledger = {'amount' : 0, 'description' : ''}
    self.format_saved_transaction = {
      'category'   : self.category,
      'activity'   : '', 'amount' : 0,
      'description': '', 'status' : False, 'balance': 0
    }
    
    fileName           = 'transaction'
    self.file          = files.Files(fileName)
    self.reload_data()

  def __str__(self):
    return f'Printing {self.category}'

  def deposit(self, amount, desc = None):
    form_ledger = self.form_ledger
    form_ledger['amount']      =  amount
    form_ledger['description'] =  desc if desc is not None else 'deposit'
    # for (key, val) in form_ledger.items() : print(f'{key} : {val}')
    # print('\n')
      
    form_saved  = self.format_saved_transaction
    form_saved['activity']    =  'deposit'
    form_saved['amount']      =  amount
    form_saved['description'] =  desc if desc is not None else 'deposit'
    form_saved['status']      =  True
    self.balance                += amount
    form_saved['balance']     =  self.balance
    self.save_data(form_saved)
    return form_ledger

  def withdraw(self, amount, desc = None):
    form_saved = self.format_saved_transaction
    form_saved['activity']    = 'withdraw'
    form_saved['amount']      = amount
    form_saved['description'] = desc if desc is not None else 'withdraw'
    form_saved['status']      = True if (self.balance > amount) else False
    self.balance                = self.balance if form_saved['status'] == False else (self.balance - amount)
    form_saved['balance']     = self.balance
    # for (key,val) in form_saved.items() : print(f'{key} : {val}')
    # print('\n')
    return form_saved['status']

  def get_balance(self, ):
    return self.balance

  def transfer(self, amount, to):
    withdraw_status = self.withdraw(amount, f"Transfer to {to}")
    transfer_status = withdraw_status
    if withdraw_status == True : 
      self.category = to
      self.deposit(amount, "Initial Deposit")
    return transfer_status

  def check_funds(self, amount) :
    return amount > self.balance

  def reload_data(self):
    self.file.reload_data()
    self.data_saved = self.file.data
    print('Reload data')

  def save_data(self, form) :
    is_saved = self.file.save_data(form)
    if is_saved == True :
      for (key,val) in form.items() : print(f'{key} : {val}')
      print('\n')
      print('Save data success')
    else : print('Save data failed')
    
def create_spend_chart(categories):
  print('create spend chart')
