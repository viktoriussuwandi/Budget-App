import traceback
import os, json

class Files :  
  def __init__(self, fileName = None) :
    self.data = []
    self.fileName = fileName if fileName is not None else None
    self.file = f'data/{self.fileName}.json'
    self.check_file()
    
  def clear_file_content(self) :
    with open(self.file, 'w') : pass
  
  def check_file(self) :
    checked = ''
    try :
      with open(self.file, 'r') : checked = f'{self.file} Exist' 
    except FileNotFoundError :
      # traceback.print_exc()
      with open(self.file, 'w') : checked = f'File {self.file} Created'
    else    : pass
    finally : 
      # print(checked)
      pass
    
    
  def save_data(self, form) :
    data_found = self.search_data(form['category'])
    if data_found == None or len(data_found) == 0 :
      self.data.append(form)
      self.clear_file_content()
      with open(f"{self.file}","w") as file : 
        json.dump(self.data, file, indent=4) 
        return True
    
  def search_data(self,category) :
    return None
    
  def reload_data(self) : 
    try :
      with open(self.file,"r") as file :
        file_size = os.path.getsize(self.file)
        self.data = json.load(file) if file_size > 0 else []
    except FileNotFoundError : self.check_file()
  