import pandas as pd
import numpy  as np

class Category:
  def __init__(self, category) :
    self.ledger = []
    self.category = category

    self.file_transaction = 'data/transaction.json'
    self.file_report      = 'report.json'
    self.update_data()

  def deposit (self, cat, amt, desc='') :
    data = self.ledger
    form = self.form
    form['Activity']    = 'deposit'
    form['status'] = False
    form['Time']        = 'now'
    form['Category']    = cat
    form['Amount']      = amt
    form['Balance']     = self.get_balance(cat)
    form['Description'] = desc
    self.update_data(form)
    return form
    
  def withdraw (self, cat, amt, desc='') :
    data = self.ledger
    form = self.form
    form['Activity']    = 'withdraw'
    form['status'] = False
    form['Time']        = 'now'
    form['Category']    = cat
    form['Amount']      = amt
    form['Balance']     = self.get_balance(cat)
    form['Description'] = desc
    self.update_data(form)
    return form

  def get_balance (self, cat) :
    data = self.ledger
    deposit  = data['Amount']
    withdraw = data['Amount']
    balance  = deposit - widthdraw
    
    # check balance, if correct -> return balance
    # data_balance = check_funds()
    return balance

  def transfer (self, amt, cat_from, cat_to, desc) :
    pass
    
def create_spend_chart(categories):
  pass
