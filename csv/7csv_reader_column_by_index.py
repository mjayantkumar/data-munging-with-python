#!/usr/bin/python
"""
Copyright 2014 Clinton W. Brownley
Available at https://github.com/cbrownley
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""
import csv
import sys

input_file = sys.argv[1]
#output_file = sys.argv[2]

my_columns = [0, 3]
with open(input_file, 'rU') as csv_in_file:
	#with open(output_file, 'wb') as csv_out_file:
		filereader = csv.reader(csv_in_file, delimiter=',')
		#filewriter = csv.writer(csv_out_file, delimiter=',')
		for row in filereader:
			row_list_output = [ ]
			for index_value in my_columns:
				row_list_output.append(row[index_value])
			print row_list_output
			#filewriter.writerow(row_list_output)