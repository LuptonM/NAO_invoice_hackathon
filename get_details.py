
from make_sentances import make_sentances
from get_rows import get_rows
from clean_images import image_to_dataframe
import pandas as pd
from string_validation import  is_total , is_numeric , is_invoice_date, is_invoice_number, is_alphanumeric_with_no_spaces , is_date, is_VAT
from get_value import get_value
import cv2
import imutils
from get_boxes_img import get_boxes


def get_details(file_path,supplier, get_inverted = False, get_rotated = False, rotation_angle = 90):
    
    boxes_df = get_boxes(file_path, get_inverted, get_rotated, rotation_angle)
    
    joined_text = boxes_df['text']
    left = boxes_df['left']
    top = boxes_df['top']
    row = boxes_df['row']
    row_part = boxes_df['row_part']

    Date_Invoiced_Index =  [(idx, text) for idx, text in enumerate(joined_text) if is_invoice_date(text)]
    
    Invoice_Number_Index = [(idx, text) for idx, text in enumerate(joined_text) if is_invoice_number(text)]

    Amount_Index = [(idx, text) for idx, text in enumerate(joined_text) if is_total(text)]

    VAT_Index = [(idx, text) for idx, text in enumerate(joined_text) if is_VAT(text)]


    supplier_match = False  

    if supplier:

       Supplier_Index = [ text for  text in joined_text if supplier in text]

       if len(Supplier_Index)>0:
          supplier_match = True
     
  
 
    if len(Invoice_Number_Index) > 0:
         Invoice_Number_Index =  Invoice_Number_Index[0][0]
         Invoice_Number = get_value(joined_text,  left, top, Invoice_Number_Index, 200, 200, row, row_part, string_validator = is_alphanumeric_with_no_spaces)
    else:
        Invoice_Number = ''     


    if len(Date_Invoiced_Index ) > 0:
      
         Date_Invoiced_Index  =  Date_Invoiced_Index[0][0]
         Date_Invoiced = get_value(joined_text,  left, top, Date_Invoiced_Index, 200, 200, row, row_part, string_validator = is_date)
      
    else:
        Date_Invoiced = ''      
   
    if len(Amount_Index ) > 0:
        
         Amount_Index  =  Amount_Index[0][0]
        
         Amount = get_value(joined_text,  left, top, Amount_Index, 800, 400, row, row_part, string_validator = is_numeric)
    else:
        Amount = ''      

    if len(VAT_Index ) > 0:
        
         VAT_Index  =  VAT_Index[0][0]
        
         VAT = get_value(joined_text,  left, top, VAT_Index, 800, 400, row, row_part, string_validator = is_numeric)
    else:
        VAT = ''            
  
    return {'Amount': Amount, 'Date_Invoiced': Date_Invoiced , 'Invoice_Number' : Invoice_Number , 'VAT': VAT , 'Supplier_Match' :  supplier_match}      


def get_invoice_details(file_path, supplier_dict):

   file_name = file_path.split('/')[-1]
   
   if file_name.endswith('.jpg'):

      file_name = file_name.split('.pdf')[0]

   if file_name.endswith('.pdf'):

      file_name = file_name.split('.pdf')[0]

   if file_name in supplier_dict:

      supplier = supplier_dict[file_name]
   else:
      supplier = ''     

   details = get_details(file_path,supplier, False, False)
 
   if details['Amount'] =='' or details['Date_Invoiced'] == '' or details['Invoice_Number'] == '' :

      details_inverted = get_details(file_path, supplier, True)
      details_rotated_plus_90 = get_details(file_path, supplier, False, True, 90)
      details_rotated_minus_90 = get_details(file_path, supplier, False, True, -90)
     
      if details['Amount'] == '' and details_inverted['Amount'] != '':
         
        details.update({'Amount': details_inverted['Amount']}) 

      if details['Amount'] == '' and details_rotated_plus_90['Amount'] != '':
         
        details.update({'Amount': details_rotated_plus_90['Amount']})  
     
      if details['Amount'] == '' and details_rotated_minus_90['Amount'] != '':
         
        details.update({'Amount': details_rotated_minus_90['Amount']})        


                       
         
      if details['Date_Invoiced'] == '' and details_inverted['Date_Invoiced'] != '':

         details.update({'Date_Invoiced': details_inverted['Date_Invoiced']}) 
         
      if details['Date_Invoiced'] == '' and details_rotated_plus_90['Date_Invoiced'] != '':

         details.update({'Date_Invoiced': details_rotated_plus_90['Date_Invoiced']})       

      if details['Date_Invoiced'] == '' and details_rotated_minus_90['Date_Invoiced'] != '':

         details.update({'Date_Invoiced': details_rotated_minus_90['Date_Invoiced']}) 




      if details['Invoice_Number'] == '' and details_inverted['Invoice_Number'] != '':

         details.update({'Invoice_Number': details_inverted['Invoice_Number']})    

      if details['Invoice_Number'] == '' and details_rotated_plus_90['Invoice_Number'] != '':

         details.update({'Invoice_Number': details_rotated_plus_90['Invoice_Number']})  
         
      if details['Invoice_Number'] == '' and details_rotated_minus_90['Invoice_Number'] != '':

         details.update({'Invoice_Number': details_rotated_minus_90['Invoice_Number']}) 
         


      if details['VAT'] == '' and details_inverted['VAT'] != '':

         details.update({'VAT': details_inverted['VAT']})    

      if details['VAT'] == '' and details_rotated_plus_90['VAT'] != '':

         details.update({'VAT': details_rotated_plus_90['VAT']})  
         
      if details['VAT'] == '' and details_rotated_minus_90['VAT'] != '':

         details.update({'VAT': details_rotated_minus_90['VAT']})     



         
   details['file_path'] = file_path.split('/')[-1]
   print(details)                                    
   return details    

