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
    try :
      with open(self.file, 'r') : self.refresh_data()
    except FileNotFoundError :
      # traceback.print_exc()
      with open(self.file, 'w') : pass
    else    : pass
    finally : pass
    
  def save_data(self, form) :
    try :
      self.refresh_data()
      self.data.append(form)
      self.clear_file_content()
      with open(f"{self.file}","w") as file : 
        json.dump(self.data, file, indent=4)
        return True
    except : return False
      
  def refresh_data(self) :
    try :
      with open(self.file,"r") as file :
        file_size = os.path.getsize(self.file)
        self.data = json.load(file) if file_size > 0 else []
        print(self.data)
    except FileNotFoundError : self.check_file(); self.refresh_data()

# ---------------------------------------------------------------------
# category = form['category']
# elements = {}
# key = [ key for (key,val) in form.items() if key != 'category' ]
# val = [ val for (key,val) in form.items() if key != 'category' ]
# for i in range(len(key)) : elements[f'{key[i]}'] = val[i]
# form_saved = {category : elements}
# self.data.append(form_saved)
  