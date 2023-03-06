import pandas as pd
import numpy  as np

class Category:
  def __init__(self, category = None) :
    self.ledger = []
    self.category = category if category is not None else None
    self.file = 'data/category.json'
    self.update_data()

  def update_data(self) :
    print('Update data')
  
  def __str__(self):
    return f'Printing {self.category}'

  def deposit (self) :
    print('deposit')
    
  def withdraw (self) :
    print('widthdraw')

  def get_balance (self) :
    print('get balance')
  
  def transfer (self) :
    print('transfer')


    
def create_spend_chart(categories):
  print('create spend chart')
