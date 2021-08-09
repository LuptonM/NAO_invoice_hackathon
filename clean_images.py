from pdf2image import convert_from_path
import pytesseract 
import cv2
import numpy as np
import imutils
import os

import shutil

def convert_pdf_to_jpeg(file_path, file_name, images_folder):
  pages = convert_from_path(file_path, 600)
  i = 1
  image_names = []
  for page in pages:
     image_name =  file_name.split('.pdf')[0] +  ".jpg"  
     page.save(images_folder+image_name, "JPEG")
     i = i+1 
     image_names.append(image_name)

  return image_names

def binarise_image(img):
  # Convert the image to gray scale
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  #de noise
  cleaned_img = cv2.fastNlMeansDenoising(gray_img)
 
  # Performing OTSU threshold
  # converting it to binary image by Thresholding 
  threshold_img = cv2.threshold(cleaned_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
  return threshold_img

def angle_to_rotate(img):
  coords = np.column_stack(np.where(img == 0))
  angle = cv2.minAreaRect(coords)[-1]
  
  # the `cv2.minAreaRect` function returns values in the
  # range [-90, 0); as the rectangle rotates clockwise the
  # returned angle trends to 0 -- in this special case we
  # need to add 90 degrees to the angle
  if angle < -45:
  	angle = -(90 + angle)
  # otherwise, just take the inverse of the angle to make
  # it positive
  else:
	  angle = -angle

  return -1*angle

def make_image_portrait(img):
  angle = angle_to_rotate(img)
  rotated_image =  imutils.rotate_bound(img, angle)
  return rotated_image


def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result  

def image_to_dataframe(img):
  str_boxes = pytesseract.image_to_data(img,lang='eng', output_type='data.frame')
  #remove NaN boxes
  str_boxes = str_boxes[str_boxes.text.notnull()]
  return str_boxes
 
def makes_all_files_jpgs(invoice_folder, images_folder): 
   pdf_imgs = [x for x in os.listdir(invoice_folder) if x.endswith(".pdf")]
   jpg_imgs = [x for x in os.listdir(invoice_folder) if x.endswith(".jpg")]

   # move all the jpg files into the images folder
   [shutil.copy(invoice_folder + x,images_folder) for x in jpg_imgs  ]
   # convert all the pdfs and move them to the images folder
   [convert_pdf_to_jpeg(invoice_folder + x, x,images_folder) for x in pdf_imgs ]

def rotate_and_overwrite_img(file_path):
  img = cv2.imread(file_path)     
  threshold_img  = binarise_image(img)
  angle = angle_to_rotate(threshold_img)
  rotated_img = imutils.rotate_bound(img, angle)
  cv2.imwrite(file_path, rotated_img) 

def clean_and_save_img(file_path, file_name, directory):  
 
  img = cv2.imread(file_path)     
  threshold_img  = binarise_image(img)
  
  cv2.imwrite(directory + file_name, threshold_img ) 


def prepare_files(invoice_folder, images_folder, cleaned_images_folder):
    makes_all_files_jpgs(invoice_folder, images_folder, cleaned_images_folder)
    all_imgs =  [x for x in os.listdir(images_folder)  if x.endswith(".jpg")]
    #rotate raw imgs
    [rotate_and_overwrite_img(images_folder + x) for x in all_imgs ]
    #saved cleaned images into cleaned image folder
    [clean_and_save_img(images_folder + x, x, cleaned_images_folder) for x in all_imgs ]
    
