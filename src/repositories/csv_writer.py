import csv
from datetime import datetime

def write_data_row(data_row):
    date_name = datetime.now().strftime("%d_%m_%Y")

    with open("service_data" +"_"+ str(date_name) +'.csv', mode='a') as employee_date_file:
        employee_writer_date = csv.writer(employee_date_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer_date.writerow(data_row)