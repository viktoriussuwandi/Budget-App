class Transactions :
  def __init__(self) :
    self.file = 'data/transactions'
    self.data = []
    self.form    = { 
      'Activity'    : '', 'status' : False,
      'Time'        : '', 'Amount' : 0 , 
      'Balance'     : 0,
      'Description' : '',
    }
    