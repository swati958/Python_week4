# writer , dictionary
from csv import writer
with open('file3.csv','w') as f:
    csv_writer = writer(f)
    # methods - writerow, writerows
    csv_writer.writerow(['name','country']) 
    csv_writer.writerow(['mohit','INDIA'])
    csv_writer.writerow(['harshit','INDIA'])

    csv_writerwriterows([['name','country'],['mohit','INDIA'],['harshit','INDIA']])