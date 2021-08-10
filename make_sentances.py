def determine_space_width ( text,  width ):
   return ( width / (len(text) ) )


def within_horiz_tolerance(left1, width, left2, tolerance):
   return (left1 + width +tolerance > left2 and left2>left1)


def within_vert_tolerance(top1, top2, tolerance):
   
   return(top1 + tolerance >= top2 and top2 - tolerance <= top1)



def is_part_of_sentance (box1_str, box1_left,box1_width , box1_top, box2_left , box2_top, tolerance):
    space_width = determine_space_width (box1_str , box1_width)
    return (within_vert_tolerance(box1_top, box2_top, tolerance) and within_horiz_tolerance( box1_left, box1_width, box2_left, space_width*2.5) )



def make_sentances (text,  left ,  top, width):

   
   joined_text = []

   joined_left = []

   joined_top = []
   joined_width = []

   is_already_joined = []

   new_text = ''

   is_already_joined = [False for i in range(len(text))]

   for i in range(len(text)):
     

     if(is_already_joined[i] == False):
     
       new_text = text[i]
       new_width = width[i]

       if i == len(text) - 1:

            joined_text.append(new_text)
            joined_left.append(left[i])
            joined_top.append(top[i])
            joined_width.append( new_width)


       for j in range(1,len(text)-i):
           
           if(is_part_of_sentance (text[i] , left[i] , new_width , top[i], left[i+j] , top[i+j], 15  )   ):
               is_already_joined[i+j] = True
               new_text = new_text + ' ' +  text[i+j]
               new_width = width[i+j] + left[i+j] - left[i]
               

           else:
               joined_text.append(new_text)
               joined_left.append(left[i])
               joined_top.append(top[i])
               joined_width.append( new_width)
              

               break
     
   return {'joined_text' : joined_text, 'joined_left' : joined_left, 'joined_top' : joined_top, 'joined_width':joined_width }


