import pandas as pd
import numpy as np
import files

class Category:

  def __init__(self, category=None):
    self.ledger        = []
    self.data_saved    = []
    self.category      = category if category is not None else None
    self.file          = files.Files('category')
    self.balance       = 0
    self.format_ledger = {'amount' : 0, 'description' : ''} 
    self.format_saved_transaction = {
      'category'   : self.category,
      'activity'   : '', 'amount' : 0,
      'description': '', 'status' : False, 'balance': 0
    }

  def update_data(self):
    print('Update data')

  def __str__(self):
    return f'Printing {self.category}'

  def deposit(self, amount, desc):
    format_ledger = self.format_ledger
    format_ledger['amount']      =  amount    
    format_ledger['description'] =  desc
    for (key, val) in format_ledger.items() : print(f'{key} : {val}')
    print('\n')
      
    format_saved  = self.format_saved_transaction
    format_saved['activity']    =  'deposit'
    format_saved['amount']      =  amount
    format_saved['description'] =  desc if desc is not None else 'deposit'
    format_saved['status']      =  True
    self.balance          += amount
    format_saved['balance']     =  self.balance
    for (key,val) in format_saved.items() : print(f'{key} : {val}')
    print('\n')
    return format_ledger

  def withdraw(self, amount, desc = None):
    format_saved = self.format_saved_transaction
    format_saved['activity']    = 'withdraw'
    format_saved['amount']      = amount
    format_saved['description'] = desc if desc is not None else 'withdraw'
    format_saved['status']      = True if (self.balance > amount) else False
    self.balance                = self.balance if format_saved['status'] == False else (self.balance - amount)
    format_saved['balance']     = self.balance
    for (key,val) in format_saved.items() : print(f'{key} : {val}')
    print('\n')
    return format_saved['status']

  def get_balance(self, ):
    return self.balance

  def transfer(self, amount, to):
    withdraw_status = self.withdraw(amount, f"Transfer to {to}")
    transfer_status = withdraw_status
    if withdraw_status == True : 
      self.category = to
      self.deposit(amount, "Initial Deposit")
    return transfer_status


def create_spend_chart(categories):
  print('create spend chart')
