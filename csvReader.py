import csv

with open('/Users/tkekan/work/prac/FL_insurance_sample.csv','rU') as file:
    count = 0
    csv_reader = csv.reader(file)
    for rows in csv_reader:
	if count > 0:
            print rows
	    break
        count += 1


