import pytesseract 
import numpy as np
import pandas as pd
import csv

import os
from pathlib import Path

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

#prepare_files(invoice_folder, images_folder, cleaned_images_folder)

cleaned_imgs = [x for x in os.listdir(cleaned_images_folder) if x.endswith(".jpg")]
input_imgs = [x for x in os.listdir(images_folder) if x.endswith(".jpg")]
details = []
#[details.append(get_invoice_details(cleaned_images_folder + x)) for x in os.listdir(cleaned_images_folder) if x.endswith(".jpg")]

#get_invoice_details(images_folder+ input_imgs[0])
get_invoice_details(cleaned_images_folder+ cleaned_imgs[15])

#dict_to_csv(details, output_folder + 'results.csv')