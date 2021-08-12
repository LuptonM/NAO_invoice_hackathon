import re
from dateutil.parser import parse

def is_total(string):
   string = string.strip().lower()
   if string == 'total' or ('total' in string and ('amount' in string or 'invoice' in string ) ):
      return True

def is_VAT(string):

   if 'vat' in string.lower():
      
      return True
   else:
      False    

def is_alphanumeric_with_no_spaces(string):

   regex = re.match('^[a-zA-Z0-9\-]*$', string)
   if regex is not None:
      matches = regex.group(0)
   else:
      matches = None  

   if matches is not None:
      return True
   else:

      return False   

def is_invoice_date(string):
   
   string = string.lower()
   if 'date' in string and 'invoice' in string:
      return True
   else:
      return False   

def is_invoice_number(string):

   string = string.lower()
   if 'invoice' in string and ('#' in string  or 'no' in string or 'number' in string ):
      return True
   else:
      return False   


def is_date(string, fuzzy=False):
    string = string.strip()
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def is_numeric(string):
   
    potential_target = string.replace('£','').strip()
    cleaned_potential_target = potential_target
    cleaned_potential_target = cleaned_potential_target.replace('.','')     
    cleaned_potential_target = cleaned_potential_target.replace(',','')  
    if cleaned_potential_target.isnumeric():
      
      return True
    else:
       return False  
