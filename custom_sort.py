import pandas as pd

def within_vert_tolerance (top1, top2, tolerance):

   if top1 + tolerance >= top2 and top1 - tolerance <= top2:
      return True
   else:
      return False   

def is_element_to_the_left(top1, top2, left1, left2, tolerance):

    if within_vert_tolerance(top1, top2, tolerance) and left1 < left2:
        return True

    else:
        return False   

def is_above(top1, top2, tolerance):

    if top1 + tolerance < top2 and top2 - tolerance > top1:
        return True
    else:
        return False


def custom_sort(text, top, left ):
        
    
    for i in range(1, len(text)):
  
        current_top = top[i]
        current_left = left[i]
        current_text = text[i]

        j = i-1
        while j >=0  and current_top < top[j]:
                
                text[j+1] = text[j]
                left[j+1] = left[j]
                top[j+1] = top[j]
                j -= 1
        left[j+1] = current_left
        top[j+1] = current_top
        text[j+1] = current_text

    for i in range(1, len(text)):
  
        current_top = top[i]
        current_left = left[i]
        current_text = text[i]

        j = i-1
        while j >=0  and within_vert_tolerance(current_top, top[j], 30) and current_left < left[j]:
                
                text[j+1] = text[j]
                left[j+1] = left[j]
                top[j+1] = top[j]
                j -= 1
        left[j+1] = current_left
        top[j+1] = current_top
        text[j+1] = current_text
      

    
       
    boxes_df = pd.DataFrame(list(zip(text, left, top )),     
               columns =['text', 'left', 'top',])


               
    return boxes_df