import xlrd
import csv
from datetime import datetime
#Target Excel file Name
filename = "expense.xlsx"
#Destination CSV file name
csvfile = "data.csv"
#sheet name from the excel file, if there are multiple sheets put it in for loop
sheetname="Sheet1"
#initialize and load sheet
book = xlrd.open_workbook(filename)
worksheet = book.sheet_by_name(sheetname)
csvfile = open(csvfile,'wb')
wr = csv.writer(csvfile,quoting= csv.QUOTE_NONE)
#First intro row
wr.writerow(worksheet.row_values(0))
#Row containing data
for row in range(1,worksheet.nrows):
    #Date Column
    date = worksheet.row_values(row)[4]
    #Date format conversion
    if isinstance(date, float) or isinstance(date, int):
        year, month, day, hour, minute, sec = xlrd.xldate_as_tuple(date, book.datemode)
        py_date = "%02d/%02d/%04d" % (month, day, year)
    #Writing into CSV file
        wr.writerow([py_date] + worksheet.row_values(row)[0:3])

csvfile.close()