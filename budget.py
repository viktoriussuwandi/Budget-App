import json

class Category :
  def __init__(self, category = None) :
    self.category = category if category is not None else None
    self.ledger  = []
    self.balance = 0
    
  def deposit(self, amount, desc = '', status_deposit = True) :
    status  = False if status_deposit == False else True
    self.balance = self.balance if status != True else (self.balance + amount)
    res = {'amount' : amount, 'description' : desc}
    self.ledger.append(res)
    return res
  
  def withdraw(self, amount, desc = '') :
    status = False if (self.balance - amount) < 0 else True
    if status == True :
      self.balance =   self.balance - amount
      res = {'amount' : -amount, 'description' : desc}
      self.ledger.append(res)
    return status
  
  def get_balance(self) :
    return self.balance

  def transfer(self, amount, to = '') :
    status    = False if (self.balance - amount) < 0 else True
    if status == True :
      desc_from = f'Transfer from {self.category}'
      desc_to   = f'Transfer to {repr(to)}'
      self.withdraw(amount, desc_to)
      to.deposit(amount, desc_from)
    return status

  def check_funds(self, amount) :
    check = (self.balance - amount) >= 0
    return check
    
  def __repr__(self): 
    return self.category
    
  def __str__(self):
    title = repr(self.category).center(30,'*').replace("'","*")
    contents = ''
    total = f'Total: {str(self.balance)}'
    for i in range(len(self.ledger)) :
      d = self.ledger[i]['description']; desc = ''
      a = format(self.ledger[i]['amount'], ".2f"); amount = ''
      if len(d) > 23 : 
        for j in range(23) : desc += d[j]
      else : desc = d
      
      if len(a) > 7  : 
        for j in range(7)  : amount += a[j]
      else : amount = a
      
      contents += desc.ljust(23,' ') + amount.rjust(7,' ')
      contents += f'\n{total}' if i == (len(self.ledger)-1) else '\n'

    res = f'{title}\n{contents}'
    return res
  
def create_spend_chart(categories) :
  chart   = 'Percentage spent by category\n'
  cat     = ''
  categories = [str(c.category) for c in categories]
  maxlenCat  = max( [ len(c) for c in categories ] )
  print(maxlenCat)
  for i in range(100,-10,-10) :
    chart += str(f'{i}').ljust(3,' ') + '|'
    chart += '\n'
  
  chart   += ''.join([' ' for i in range(3)])
  chart   += ''.join(['-' for i in range(len(categories) + 1)])
  chart   += '\n'

  for c in range(categories) :
    print(c)
  
  
  return chart
    