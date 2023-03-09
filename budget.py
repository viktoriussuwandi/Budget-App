import pandas as pd
import numpy as np
import files, json

class Category:

  def __init__(self, category = None):
    self.ledger        = []
    self.data_saved    = []
    self.category      = category if category is not None else None
    self.balance       = 0
    self.form_ledger = {'amount' : 0, 'description' : ' '}
    self.format_saved_transaction = {
      'category'   : self.category,
      'activity'   : '', 'amount' : 0,
      'description': ' ', 'status' : False, 'balance': 0
    }
    
    self.fileName      = 'transactions'
    self.file          = files.Files(self.fileName)


# ---------------------------------------------------------------------------------------------------
# CLASS CATERORY - MAIN FUNCTIONS
# ---------------------------------------------------------------------------------------------------
    
  def deposit(self, amount, desc = '', status = None) :
    form  = self.format_saved_transaction
    form['activity']    =  'deposit'
    form['amount']      =  amount
    form['description'] =  desc
    form['status']      =  True if (status == None or status != False) else False
    self.balance        = self.balance if form['status'] != False else (self.balance + amount)
    form['balance']     = self.balance
    self.save_data(form)
    
    form_ledger = self.form_ledger
    form_ledger['amount']      : amount
    form_ledger['description'] : desc
    return form_ledger

  def withdraw(self, amount, desc = ''):
    form = self.format_saved_transaction
    form['activity']    = 'withdraw'
    form['amount']      = -amount
    form['description'] = desc
    form['status']      = True if (self.balance > amount) else False
    self.balance        = self.balance if form['status'] == False else (self.balance - amount)
    form['balance']     = self.balance
    # if form['status'] == True : self.save_data(form)
    self.save_data(form)
    return form['status']
    
  def transfer(self, amount, To):
    beg_balance = self.balance
    check = self.balance > amount
    # if check :
    desc_to    = f'Transfer to {repr(To)}'
    desc_from  = f'Transfer from {repr(self.category)}'
    self.withdraw(amount, desc_to)
    To.deposit(amount, desc_from, check)
    return beg_balance > amount
    
  def get_balance(self):
    # print(json.dumps(self.ledger, indent = 4))
    # print('\n')
    # print(json.dumps(self.data_saved, indent = 4))
    return self.balance

  def check_funds(self, amount) :
    return amount < self.balance
    
# ---------------------------------------------------------------------------------------------------
# CLASS CATERORY - SUPPORTING FUNCTIONS
# ---------------------------------------------------------------------------------------------------

  def __repr__(self): 
    return self.category
    
  def __str__(self):
    self.refresh_data()
    ledger = json.dumps(self.ledger, indent = 4)
    return ledger
    # return f'Printing {self.category}'
    
# ---------------------------------------------------------------------------------------------------
# CLASS CATERORY - DATA MANAGEMENT FUNCTIONS
# ---------------------------------------------------------------------------------------------------
  def refresh_data(self):
    reload_data = self.file.data
    if len(reload_data) > 0 :
      self.data_saved = self.file.data
      self.ledger  = []
      for d in self.data_saved :
        if (d['category'] == self.category and d['status'] == True) :
          self.ledger.append( { 'amount' : d['amount'], 'description' : d['description'] } )
          if   (d['activity'] == 'deposit')   : self.balance += d['amount']
          elif (d['activity'] == 'widthdraw') : self.balance -= d['amount']
    
  def save_data(self, form) :
    self.file.save_data(form)
    self.refresh_data()
    # return is_saved
    
# ---------------------------------------------------------------------------------------------------
# CHART FUNCTION
# --------------------------------------------------------------------------------------------------   
def create_spend_chart(categories):
  print('create spend chart')

  # -----------------------------------------------------------------------------------

  # def transfer(self, amount, to):
  #   withdraw_status = self.withdraw(amount, f"Transfer to {to}")
  #   transfer_status = withdraw_status
  #   if withdraw_status == True : 
  #     self.category = to
  #     self.deposit(amount, "Initial Deposit")
  #   return transfer_status

  # def check_funds(self, amount) :
  #   return amount > self.balance
