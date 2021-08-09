

def within_tolerance(top1, top2, tolerance):

    if (top2 + tolerance >= top1 and top2 - tolerance <= top1):

        return True
    else:

        return False



def get_rows(top, tolerance = 10):
    # initialise empty list/vector
    row = [1] * len(top)
    row_part = [1] * len(top)
  
    current_row = 1
    current_row_part = 1
    current_top = top[0]

    for i in range(1, len(top)):
             
        if within_tolerance(current_top, top[i], tolerance):
            current_row_part += 1
            
        else:
            current_row += 1 
            current_row_part = 1    

        row[i]  = current_row    
        row_part[i] = current_row_part
        current_top = top[i]

    return {'row': row , 'row_part' : row_part}

