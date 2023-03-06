import traceback
import os

class Files :  
  def __init__(self, fileName = None) :
    self.fileName = fileName if fileName is not None else None
    self.file = f'data/{self.fileName}.json'
    self.check_file()
    
  def clear_file_content(self) :
    with open(self.file, 'w') : pass
  
  def check_file(self) :
    try :
      with open(self.file, 'r') : print(f'{self.file} Exist') 
    except FileNotFoundError :
      # traceback.print_exc()
      with open(self.file, 'w') : print(f'File {self.file} Created')
    else    : pass
    finally : pass

  def save_data(self, fileName, data) :
    self.fileName = fileName
    pass    