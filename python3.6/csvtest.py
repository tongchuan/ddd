
import csv

with open('names.csv','w') as csvfile:
    filednames = ['first_name','last_name']
    writer = csv.DictWriter(csvfile, fieldnames=filednames)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
