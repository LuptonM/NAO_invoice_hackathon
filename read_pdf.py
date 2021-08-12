import pytesseract 
import numpy as np
import pandas as pd
import csv

import os
from pathlib import Path
from get_poppler_boxes import get_poppler_boxes
from get_details import get_invoice_details
from save_dict_to_csv import dict_to_csv
from clean_images import prepare_files
import re
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

base_path = Path(__file__).parent

invoice_folder = str((base_path / "./invoices/").resolve()) + '/'
images_folder = str((base_path / "./images/").resolve()) + '/'
cleaned_images_folder = str((base_path / "./cleaned_images/").resolve()) + '/'
output_folder = str((base_path / "./output/").resolve()) + '/'


supplier_dict = { '503286G7W8-SPAU-Ice-cream-Ltd': 'Premier Chocolate', 
                  'ICE4903-SPAU-Ice-cream-Ltd' :'Peacock Salt' ,
                  '112840X-SPAU-Ice-cream-Ltd': 'The Strawberry Basket',
                  '67895GR8S-SPAU-Ice-cream-Ltd' : 'Premier Chocolate',
                  '9857389200-SPAU-Ice-cream-Ltd' : 'Mentmoore Foods',
                  '1197284091-SPAU-Ice-cream-Ltd' : 'Mentmoore Foods',
                  '9986749370-SPAU-Ice-cream-Ltd' : 'Mentmoore Foods',
                  'PUF3928610-SPAU-Ice-cream-Ltd': 'Asala Agriculture',
                  '329-74688-SPAU-Ice-cream-Ltd': 'ATILIM TAVUKCULUK TARIM URUNLERI',
                  '4382502-SPAU-Ice-cream-Ltd'  : 'The Strawberry Basket',
                  '1249327590-SPAU-Ice-cream-Ltd' : 'Mentmoore Foods',
                  '9804937992WB-SPAU-Ice-cream-Ltd' : 'West Berry',
                  'THR589023-SPAU-Ice-cream-Ltd' : 'Asala Agriculture',
                  '7254219-SPAU-Ice-cream-Ltd': 'The Strawberry Basket',
                  '3284510821-SPAU-Ice-cream-Ltd' : 'Mentmoore Foods',
                  '9867254-SPAU-Ice-cream-Ltd': 'The Strawberry Basket',
                  '82-3523-8459-SPAU-Ice-cream-Ltd':'Meat Inn ',
                  'JYT3626010-SPAU-Ice-cream-Ltd' : 'Asala Agriculture',
                  '1937534963-SPAU-Ice-cream-Ltd' : 'Mentmoore Foods',
                  '7762629100-SPAU-Ice-cream-Ltd' : 'Mentmoore Foods'
                   }

#prepare_files(invoice_folder, images_folder, cleaned_images_folder)

cleaned_imgs = [x for x in os.listdir(cleaned_images_folder) if x.endswith(".jpg")]
input_imgs = [x for x in os.listdir(images_folder) if x.endswith(".jpg")]
input_imgs = [x for x in os.listdir(images_folder) if x.endswith(".jpg")]

invoices = [x for x in os.listdir(invoice_folder) ]
details = []




    
[details.append(get_invoice_details(cleaned_images_folder + x, supplier_dict)) for x in os.listdir(cleaned_images_folder) if x.endswith(".jpg")]

#get_invoice_details(images_folder+ input_imgs[0])
#get_invoice_details(cleaned_images_folder+ cleaned_imgs[16], supplier_dict)

dict_to_csv(details, output_folder + 'results.csv')



