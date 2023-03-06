class Transactions :
  def __init__(self) :
    self.data = []
    self.file = 'data/transactions.json'
    self.form    = { 
      'Activity'    : '', 'status' : False,
      'Time'        : '', 'Amount' : 0 , 
      'Balance'     : 0,
      'Description' : '',
    }
    