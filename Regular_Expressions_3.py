#Author:  R. Webster, Optum Technology  7 August 2022
#Purpose:  Python Mentoring
#This module illustrates:
# An initial search using regular expressions
# In this case the parsing of a string to determine if the date time string
#  entry is correctly formatted

import datetime
date_string = '2017-12-31'
date_format = '%Y-%m-%d'
# A new concept of try / except illustrated here
try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  print(date_obj)
except ValueError:
  print("Incorrect data format, should be YYYY-MM-DD")
