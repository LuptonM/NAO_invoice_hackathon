from make_sentances import make_sentances
from get_rows import get_rows
from clean_images import image_to_dataframe
import pandas as pd
from string_validation import  is_total , is_numeric , is_invoice_date, is_invoice_number, is_alphanumeric_with_no_spaces , is_date
from get_value import get_value
import cv2
import imutils
from custom_sort import custom_sort
from clean_images import read_clean_and_rotate_img

def get_boxes_dataframe(img):
 
   boxes_df = image_to_dataframe(img)
    
   #boxes_df = boxes_df[boxes_df['conf'] > 50]
   
   
 
   sentance_dict = make_sentances ( list(boxes_df['text']),list(boxes_df['left']) , list(boxes_df['top']),  list(boxes_df['width'] ))      
    
   
  
   joined_text = sentance_dict['joined_text']

   left = sentance_dict['joined_left'] 
   top = sentance_dict['joined_top'] 

            
   boxes_df = custom_sort (joined_text, top, left)            
   
    
   row_dict = get_rows(boxes_df['top'].tolist())

   row = row_dict['row']
   row_part = row_dict['row_part']
    
   boxes_df['row'] = row
   boxes_df['row_part'] = row_part 
   
  
   return boxes_df            


def get_boxes(file_path, get_inverted = False, get_rotated = False, rotation_angle = 90):
    img = cv2.imread(file_path)
    
    if get_rotated == False:
      boxes_df = get_boxes_dataframe(img)
    if get_inverted and get_rotated == False:
      inverted_img = cv2.bitwise_not(img)
      boxes_df_inverted = get_boxes_dataframe(inverted_img)
      boxes_df = boxes_df.append(boxes_df_inverted).drop_duplicates()
      boxes_df = boxes_df.sort_values(by = ['row', 'left']).reset_index(drop=True) 

    if get_rotated:  
      rotated_img = imutils.rotate_bound(img, rotation_angle)
      boxes_df = get_boxes_dataframe(rotated_img)
   
    return boxes_df
