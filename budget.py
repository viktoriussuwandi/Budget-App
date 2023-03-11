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
  blank   = '.'
  len_start_dots = len(str(100)) + 1

  # calculate withdrawal percentage---------------------------------------
  ledgers     = [ l for l in [ c.ledger for c in categories] ]
  withdrawals = [ ]
  for l in ledgers :
    withdrawals.append([
        dict['amount'] for dict in l if (
        dict['amount'] < 0 and 'Transfer' not in dict['description']
      )][0])
  percents = [ 100*( w/sum(withdrawals) ) for w in withdrawals ]
  
  # print(json.dumps(ledgers,indent = 4))
  # print(json.dumps(withdrawals,indent = 4))
  # print(json.dumps(percents,indent = 4))
  
  
  # print point axis------------------------------------------------------
  for i in range(100,-10,-10) :
    chart += str(f'{i}').rjust(3,blank) + '|'
    for c in range(len(categories)) :
      cat = categories[c]
      len_start_val   = 1 if c == 0 else 0
      len_end_val     = 2
      start_space_val = ''.join([blank for s in range(len_start_val)])
      end_space_val   = ''.join([blank for s in range(len_end_val)])
      chart += start_space_val
      percent = round(percents[c],0)
      if percent >= i : chart += 'o'
      else : chart += blank
      chart += end_space_val
    chart += '\n'

  # print the dots--------------------------------------------------------
  start_dots     = ''.join([blank for i in range(len_start_dots)])
  len_dots       = pow(len(categories),2) + 1
  dots           = ''.join(['-' for i in range(len_dots)])
  chart         += start_dots + dots + '\n'

  # print categories axis-------------------------------------------------
  categories = [str(c.category) for c in categories]
  list = [ c.title() for c in categories]
  maxlenCat  = max( [ len(l) for l in list ] )
  cat_axis = ''
  for m in range(maxlenCat) :
    for i in range(len(list)) :
      cat = list[i]
      len_start_cat   = (len_start_dots + 1) if i == 0 else 0
      len_end_cat     = 2
      start_space_cat = ''.join([blank for s in range(len_start_cat)])
      end_space_cat   = ''.join([blank for s in range(len_end_cat)])
      cat_axis += start_space_cat
      if m < len(cat) : cat_axis += f'{cat[m]}'
      else : cat_axis += f'{blank}'
      cat_axis += end_space_cat
    cat_axis += '\n'
    
  chart += cat_axis
  return chart