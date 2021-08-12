import pandas as pd
from poppler import load_from_file
from get_rows import get_rows


def make_sentances(text, left, top , width , height, right, has_space_after):

     joined_text = []

     joined_left = []

     joined_top = []
     joined_width = []
     joined_height = []
     joined_right = []
     is_already_joined = []

     new_text = ''

     is_already_joined = [False for i in range(len(text))]

     for i in range(len(text)):
     

       if(is_already_joined[i] == False):
     
         new_text = text[i]
         new_width = width[i]
         new_right = right[i]

         if i == len(text) - 1:

            joined_text.append(new_text)
            joined_left.append(left[i])
            joined_top.append(top[i])
            joined_width.append( new_width)
            joined_height.append(height[i])
            joined_right.append(new_right)
            

         for j in range(1,len(text)-i):
           
           if has_space_after[i + j-1]:
               is_already_joined[i+j] = True
               new_text = new_text + ' ' +  text[i+j]
               new_width = width[i+j] + left[i+j] - left[i]
               new_right = right[i+j]
               

           else:
               joined_text.append(new_text)
               joined_left.append(left[i])
               joined_top.append(top[i])
               joined_width.append( new_width)
               joined_height.append(height[i])
               joined_right.append(new_right)
              

               break
     
     return {'joined_text' : joined_text, 'joined_left' : joined_left, 'joined_top' : joined_top, 'joined_width':joined_width , 'joined_height':joined_height, 'joined_right': joined_right}

def get_poppler_boxes(pdf_file, page_no):
   assert(page_no > 0) 
   boxes = [] 
   pdf_document = load_from_file(pdf_file)
   page = pdf_document.create_page(page_no - 1)
   page_text = page.text_list()
   [ boxes.append({'text': text.text, 'has_space_after': text.has_space_after , 'left': text.bbox.left, 'top': text.bbox.top, 'right': text.bbox.right, 'width': text.bbox.width , 'height' : text.bbox.height}) for  text in page_text]
   boxes_df = pd.DataFrame(boxes)
   sentances = make_sentances(list(boxes_df['text']), list(boxes_df['left']), list(boxes_df['top']) , list(boxes_df['width']) , list(boxes_df['height']), list(boxes_df['right']), list(boxes_df['has_space_after']))
   
   boxes_df  = pd.DataFrame(list(zip(sentances['joined_text'], sentances['joined_left'], sentances['joined_top'], sentances['joined_right'], sentances['joined_height']  )),     
               columns =['text', 'left', 'top', 'right','height'])


   row_dict = get_rows(boxes_df['top'].tolist() , 10)

   row = row_dict['row']
   row_part = row_dict['row_part']
    
   boxes_df['row'] = row
   boxes_df['row_part'] = row_part             

   return boxes_df

