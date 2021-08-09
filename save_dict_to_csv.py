import csv

def dict_to_csv(dictionary, output_filepath):

  try:
      with open(output_filepath, 'w') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames= dictionary[0].keys())
          writer.writeheader()
          for data in dictionary:
              writer.writerow(data)
  except IOError:
      print("I/O error")