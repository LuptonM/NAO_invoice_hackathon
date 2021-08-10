def within_coord_tolerance(left, top ,  search_left_start, search_top_start, search_left_range, search_top_range):

   if (left >= search_left_start and left <= search_left_start + search_left_range and  top >= search_top_start and top <= search_top_start + search_top_range):
      return True
   else:
      return False   

def is_next_row_part(row1, row2, row_part1, row_part2):

   if(row1 == row2 and row_part1 + 1 == row_part2):
      return True
   else:
      return False

def is_row_item_below(row1, row2, row_part1, row_part2):
 
  if(row1 + 1 == row2 ) and (row_part1 == row_part2):
      return True
  else:
      return  False


def is_wrongly_classified_as_prev_row_part(left1, left2 ,row1 , row2, row_part1, row_part2):
   if  left2 > left1 and row1 == row2 and row_part1  == row_part2 + 1 :
      return True
   else:
      return False           

def within_search_area(left, top ,  search_left_start, search_top_start, search_left_range, search_top_range, row1, row2, row_part1, row_part2):

   if (within_coord_tolerance(left, top ,  search_left_start, search_top_start, search_left_range, search_top_range) and row1 == row2) or is_next_row_part(row1, row2, row_part1, row_part2) or is_row_item_below(row1, row2, row_part1, row_part2) or is_wrongly_classified_as_prev_row_part(search_left_start, left ,row1 , row2, row_part1, row_part2):
      return True
   else:
      return False

   

def get_value(text,  left, top, start_index, search_left_range, search_top_range,row, row_part, string_validator):

   
   value = ''
   
   for i in range (len(text)):       

     if within_search_area(left[i], top[i], left[start_index], top[start_index], search_left_range, search_top_range, row[start_index] , row[i], row_part[start_index], row_part[i]):
       
        if string_validator(text[i]):
           value = text[i]
         
   return value.strip()
